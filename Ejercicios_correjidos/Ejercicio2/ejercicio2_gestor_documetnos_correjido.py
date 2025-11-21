from datetime import datetime
import json
from abc import ABC, abstractmethod

class ReportType(ABC):
    @abstractmethod
    def generate_content(self, data, timestamp):
        pass

class SalesReport(ReportType):
    def generate_content(self, data, timestamp):
        content = "="*60 + "\n"
        content += "           REPORTE DE VENTAS\n"
        content += "="*60 + "\n"
        content += f"Fecha de generacion: {timestamp}\n\n"
        
        total_sales = sum(item['amount'] for item in data['sales'])
        content += f"Total de ventas: ${total_sales:.2f}\n"
        content += f"Numero de transacciones: {len(data['sales'])}\n"
        content += f"Periodo: {data['period']}\n\n"
        
        content += "Detalle de ventas:\n"
        content += "-" * 60 + "\n"
        for sale in data['sales']:
            content += f"  • Producto: {sale['product']} - ${sale['amount']:.2f}\n"
        
        return content

class InventoryReport(ReportType):
    def generate_content(self, data, timestamp):
        content = "="*60 + "\n"
        content += "           REPORTE DE INVENTARIO\n"
        content += "="*60 + "\n"
        content += f"Fecha de generacion: {timestamp}\n\n"
        
        total_items = sum(item['quantity'] for item in data['items'])
        content += f"Total de productos: {total_items}\n"
        content += f"Categorias: {len(set(item['category'] for item in data['items']))}\n\n"
        
        content += "Inventario actual:\n"
        content += "-" * 60 + "\n"
        for item in data['items']:
            content += f"  • {item['name']} ({item['category']}): {item['quantity']} unidades\n"
        
        return content

class FinancialReport(ReportType):
    def generate_content(self, data, timestamp):
        content = "="*60 + "\n"
        content += "           REPORTE FINANCIERO\n"
        content += "="*60 + "\n"
        content += f"Fecha de generacion: {timestamp}\n\n"
        
        content += f"Ingresos: ${data['income']:.2f}\n"
        content += f"Gastos: ${data['expenses']:.2f}\n"
        content += f"Balance: ${data['income'] - data['expenses']:.2f}\n"
        
        return content

class OutputFormat(ABC):
    @abstractmethod
    def format_content(self, content):
        pass

class PDFFormat(OutputFormat):
    def format_content(self, content):
        print("Generando reporte en formato PDF...")
        return f"[PDF FORMAT]\n{content}\n[END PDF]"

class ExcelFormat(OutputFormat):
    def format_content(self, content):
        print("Generando reporte en formato Excel...")
        return f"[EXCEL FORMAT]\n{content}\n[END EXCEL]"

class HTMLFormat(OutputFormat):
    def format_content(self, content):
        print("Generando reporte en formato HTML...")
        return f"<html><body><pre>{content}</pre></body></html>"

class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self, report_type):
        pass

class EmailDelivery(DeliveryMethod):
    def deliver(self, report_type):
        print("Enviando reporte por email...")
        print("   Destinatario: admin@company.com")

class DownloadDelivery(DeliveryMethod):
    def deliver(self, report_type):
        filename = f"report_{report_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"Reporte disponible para descarga: {filename}")

class CloudDelivery(DeliveryMethod):
    def deliver(self, report_type):
        print("Subiendo reporte a la nube...")
        print(f"   URL: https://cloud.company.com/reports/{report_type}")

class ReportFactory:
    @staticmethod
    def create_report_type(report_type):
        report_types = {
            'sales': SalesReport(),
            'inventory': InventoryReport(),
            'financial': FinancialReport()
        }
        return report_types.get(report_type)
    
    @staticmethod
    def create_output_format(format_type):
        output_formats = {
            'pdf': PDFFormat(),
            'excel': ExcelFormat(),
            'html': HTMLFormat()
        }
        return output_formats.get(format_type)
    
    @staticmethod
    def create_delivery_method(method_type):
        delivery_methods = {
            'email': EmailDelivery(),
            'download': DownloadDelivery(),
            'cloud': CloudDelivery()
        }
        return delivery_methods.get(method_type)

class ReportSystem:
    def __init__(self):
        self.reports_generated = []
        self.factory = ReportFactory()
    
    def generate_report(self, report_type, data, output_format, delivery_method):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"\n{'='*50}")
        print(f"Procesando reporte: {report_type}")
        print(f"Formato: {output_format}")
        print(f"Entrega: {delivery_method}")
        print(f"{'='*50}\n")
        
        report_generator = self.factory.create_report_type(report_type)
        if not report_generator:
            print(f"Tipo de reporte no soportado: {report_type}")
            return None
        
        formatter = self.factory.create_output_format(output_format)
        if not formatter:
            print(f"Formato de salida no soportado: {output_format}")
            return None
        
        delivery_handler = self.factory.create_delivery_method(delivery_method)
        if not delivery_handler:
            print(f"Metodo de entrega no soportado: {delivery_method}")
            return None
        
        report_content = report_generator.generate_content(data, timestamp)
        formatted_report = formatter.format_content(report_content)
        delivery_handler.deliver(report_type)
        
        self.reports_generated.append({
            'type': report_type,
            'format': output_format,
            'delivery': delivery_method,
            'timestamp': timestamp
        })
        
        print(f"\nReporte generado exitosamente\n")
        print(formatted_report)
        print("\n" + "="*60 + "\n")
        
        return formatted_report
    
    def get_report_history(self):
        return self.reports_generated

if __name__ == "__main__":
    system = ReportSystem()
    
    sales_data = {
        'period': 'Enero 2024',
        'sales': [
            {'product': 'Laptop HP', 'amount': 899.99},
            {'product': 'Mouse Logitech', 'amount': 25.50},
            {'product': 'Teclado Mecanico', 'amount': 120.00},
            {'product': 'Monitor LG 24"', 'amount': 199.99}
        ]
    }
    
    system.generate_report('sales', sales_data, 'pdf', 'email')
    
    inventory_data = {
        'items': [
            {'name': 'Laptop HP', 'category': 'Computadoras', 'quantity': 15},
            {'name': 'Mouse Logitech', 'category': 'Accesorios', 'quantity': 50},
            {'name': 'Teclado Mecanico', 'category': 'Accesorios', 'quantity': 30},
            {'name': 'Monitor LG', 'category': 'Pantallas', 'quantity': 20}
        ]
    }
    
    system.generate_report('inventory', inventory_data, 'excel', 'download')
    
    financial_data = {
        'income': 50000.00,
        'expenses': 32000.00
    }
    
    system.generate_report('financial', financial_data, 'html', 'cloud')
    
    print("\nHISTORIAL DE REPORTES GENERADOS:")
    print(json.dumps(system.get_report_history(), indent=2))

"""
PATRONES APLICADOS:
- Strategy: ReportType, OutputFormat y DeliveryMethod con sus implementaciones definen familias de algoritimos
- Factory: ReportFactory centraliza la creacion de objetos para reportes, formatos y metodos de entrega

PRINCIPIOS SOLID APLICADOS:
- S (Single Responsibility): Cada clase tiene una unica responsabilidad especifica
- O (Open/Closed): El sistema esta abierto para extension pero cerrado para modificacion
"""