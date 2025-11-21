import json
from datetime import datetime
from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, customer, order_id, total):
        pass
    
    @abstractmethod
    def get_notification_data(self, customer, order_id, total):
        pass

class EmailNotification(NotificationChannel):
    def send(self, customer, order_id, total):
        message_data = self.get_notification_data(customer, order_id, total)
        print(f"EMAIL enviado a {customer['email']}")
        print(f"   Asunto: Confirmacion de Pedido #{order_id}")
        print(f"   Mensaje: {message_data['message']}\n")
        return message_data
    
    def get_notification_data(self, customer, order_id, total):
        message = f"Estimado {customer['name']}, su pedido #{order_id} por ${total} ha sido confirmado."
        return {
            'type': 'email',
            'to': customer['email'],
            'message': message,
            'timestamp': datetime.now().isoformat()
        }

class SMSNotification(NotificationChannel):
    def send(self, customer, order_id, total):
        message_data = self.get_notification_data(customer, order_id, total)
        print(f"SMS enviado a {customer['phone']}")
        print(f"   Mensaje: {message_data['message']}\n")
        return message_data
    
    def get_notification_data(self, customer, order_id, total):
        message = f"Pedido #{order_id} confirmado. Total: ${total}. Gracias por su compra!"
        return {
            'type': 'sms',
            'to': customer['phone'],
            'message': message,
            'timestamp': datetime.now().isoformat()
        }

class PushNotification(NotificationChannel):
    def send(self, customer, order_id, total):
        message_data = self.get_notification_data(customer, order_id, total)
        print(f"PUSH enviada al dispositivo {customer['device_id']}")
        print(f"   Mensaje: {message_data['message']}\n")
        return message_data
    
    def get_notification_data(self, customer, order_id, total):
        message = f"¡Pedido confirmado! #{order_id} - ${total}"
        return {
            'type': 'push',
            'to': customer['device_id'],
            'message': message,
            'timestamp': datetime.now().isoformat()
        }

class NotificationFactory:
    @staticmethod
    def create_notification(channel_type):
        channels = {
            'email': EmailNotification(),
            'sms': SMSNotification(),
            'push': PushNotification()
        }
        return channels.get(channel_type)

class OrderNotificationSystem:
    def __init__(self):
        self.notifications_sent = []
        self.factory = NotificationFactory()
    
    def process_order(self, order_data, notification_types):
        order_id = order_data['order_id']
        customer = order_data['customer']
        total = order_data['total']
        
        print(f"\n{'='*50}")
        print(f"Procesando pedido #{order_id}")
        print(f"Cliente: {customer['name']}")
        print(f"Total: ${total}")
        print(f"{'='*50}\n")
        
        for notif_type in notification_types:
            channel = self.factory.create_notification(notif_type)
            if channel:
                notification_data = channel.send(customer, order_id, total)
                self.notifications_sent.append(notification_data)
            else:
                print(f"Canal de notificacion no soportado: {notif_type}")
    
    def get_notification_history(self):
        return self.notifications_sent

if __name__ == "__main__":
    system = OrderNotificationSystem()
    
    order1 = {
        'order_id': 'ORD-001',
        'customer': {
            'name': 'Ana Garcia',
            'email': 'ana.garcia@email.com',
            'phone': '+34-600-123-456',
            'device_id': 'DEVICE-ABC-123'
        },
        'total': 150.50
    }
    
    system.process_order(order1, ['email', 'sms', 'push'])
    
    order2 = {
        'order_id': 'ORD-002',
        'customer': {
            'name': 'Carlos Ruiz',
            'email': 'carlos.ruiz@email.com',
            'phone': '+34-600-789-012',
            'device_id': 'DEVICE-XYZ-789'
        },
        'total': 75.00
    }
    
    system.process_order(order2, ['email'])
    
    print("\n" + "="*50)
    print("HISTORIAL DE NOTIFICACIONES")
    print("="*50)
    history = system.get_notification_history()
    print(json.dumps(history, indent=2, ensure_ascii=False))

"""
PATRONES QUE APLIQUÉ:
- Strategy: NotificationChannel y sus implementtaciones (Email, SMS, Push) definen diferentes algoritmos de notificación
- Factory: NotificationFactory centraliza la creacion de objetos de notificación

PRINCIPIOS SOLID APLICADOS:
- S (Single Responsibility): Cada clase de notificacio  tiene una única responsabilidad específica
- O (Open/Closed): El sistema está abierto para extension (nuevos canales) pero cerrado para modificación
"""