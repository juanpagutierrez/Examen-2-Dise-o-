# 📚 Examen 2 - Diseño de Software

Proyecto académico que demuestra la aplicación de **patrones de diseño** y **principios SOLID** en Python, transformando código procedural en arquitecturas orientadas a objetos escalables y mantenibles.

## 🎯 Objetivo

Refactorizar código con problemas de diseño aplicando:
- **Patrones de Diseño**: Strategy y Factory
- **Principios SOLID**: Single Responsibility, Open/Closed
- **Buenas prácticas**: Abstracción, encapsulación y modularidad

## 📂 Estructura del Proyecto

```
Examen 2 ( Diseño de Software )/
│
├── Ejercicios/                          # Código original (antes de refactorizar)
│   ├── ejercicio1_tienda_online.py      # Sistema de notificaciones (versión procedural)
│   └── ejercicio2_gestor_documentos.py  # Generador de reportes (versión procedural)
│
└── Ejercicios_correjidos/               # Código refactorizado con patrones
    ├── Ejercicio1/
    │   ├── ejercicio1_tienda_online_correjido.py
    │   ├── c1.puml                      # Diagrama de clases
    │   ├── c2.puml                      # Diagrama de secuencia
    │   └── c3.puml                      # Diagrama de componentes
    │
    └── Ejercicio2/
        ├── ejercicio2_gestor_documetnos_correjido.py
        ├── c1.puml                      # Diagrama de clases
        ├── c2.puml                      # Diagrama de secuencia
        └── c3.puml                      # Diagrama de componentes
```

## 🚀 Ejercicios Implementados

### Ejercicio 1: Sistema de Notificaciones de Pedidos

**Problema Original:**
- Código procedural con múltiples `if/elif` para manejar diferentes canales de notificación
- Difícil de mantener y extender
- Violación del principio Open/Closed

**Solución Implementada:**
- ✅ **Strategy Pattern**: Cada canal de notificación (Email, SMS, Push) es una estrategia independiente
- ✅ **Factory Pattern**: `NotificationFactory` centraliza la creación de notificadores
- ✅ **Abstracción**: Interfaz común `NotificationChannel` con `ABC`

**Patrones Aplicados:**
```python
# Strategy Pattern
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, customer, order_id, total):
        pass

# Implementaciones concretas
class EmailNotification(NotificationChannel): ...
class SMSNotification(NotificationChannel): ...
class PushNotification(NotificationChannel): ...

# Factory Pattern
class NotificationFactory:
    @staticmethod
    def create_notification(channel_type): ...
```

### Ejercicio 2: Sistema de Generación de Reportes

**Problema Original:**
- Lógica de generación, formateo y entrega mezclada en un solo método
- Difícil agregar nuevos tipos de reportes o formatos
- Alto acoplamiento

**Solución Implementada:**
- ✅ **Strategy Pattern**: Separación de responsabilidades en tres familias de estrategias
  - Tipos de reporte (Sales, Inventory, Financial)
  - Formatos de salida (PDF, Excel, HTML)
  - Métodos de entrega (Email, Download, Cloud)
- ✅ **Factory Pattern**: `ReportFactory` con tres métodos de creación especializados
- ✅ **Composición**: Sistema flexible que combina estrategias dinámicamente

**Patrones Aplicados:**
```python
# Strategy Pattern - Tres familias de algoritmos
class ReportType(ABC): ...
class OutputFormat(ABC): ...
class DeliveryMethod(ABC): ...

# Factory Pattern - Creación centralizada
class ReportFactory:
    @staticmethod
    def create_report_type(report_type): ...
    @staticmethod
    def create_output_format(format_type): ...
    @staticmethod
    def create_delivery_method(method_type): ...
```

## 💡 Principios SOLID Aplicados

| Principio | Aplicación |
|-----------|------------|
| **S** - Single Responsibility | Cada clase tiene una única responsabilidad bien definida |
| **O** - Open/Closed | Abierto para extensión (nuevas estrategias), cerrado para modificación |
| **L** - Liskov Substitution | Todas las implementaciones son intercambiables |
| **I** - Interface Segregation | Interfaces específicas y cohesivas |
| **D** - Dependency Inversion | Dependencia de abstracciones (ABC), no de implementaciones concretas |

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **ABC (Abstract Base Classes)**: Para definir interfaces
- **datetime**: Manejo de timestamps
- **json**: Serialización de datos
- **PlantUML**: Diagramas UML (`.puml`)

## 📦 Instalación y Ejecución

### Prerrequisitos
```bash
python --version  # Python 3.6+
```

### Ejecución

**Ejercicio 1 - Sistema de Notificaciones:**
```bash
# Versión original
python Ejercicios/ejercicio1_tienda_online.py

# Versión refactorizada
python Ejercicios_correjidos/Ejercicio1/ejercicio1_tienda_online_correjido.py
```

**Ejercicio 2 - Generador de Reportes:**
```bash
# Versión original
python Ejercicios/ejercicio2_gestor_documentos.py

# Versión refactorizada
python Ejercicios_correjidos/Ejercicio2/ejercicio2_gestor_documetnos_correjido.py
```

## 📊 Comparación: Antes vs Después

### Métricas de Calidad

| Aspecto | Código Original | Código Refactorizado |
|---------|----------------|----------------------|
| **Complejidad Ciclomática** | Alta (múltiples if/elif) | Baja (polimorfismo) |
| **Acoplamiento** | Alto | Bajo |
| **Cohesión** | Baja | Alta |
| **Extensibilidad** | Difícil | Fácil (agregar clases) |
| **Testabilidad** | Compleja | Simple (mocking) |

### Ejemplo de Extensión

**Agregar un nuevo canal de notificación:**

❌ **Antes**: Modificar método `process_order`, agregar más `elif`
```python
elif notif_type == 'whatsapp':  # ¡Modifica código existente!
    # Nueva lógica...
```

✅ **Después**: Crear nueva clase, registrar en factory
```python
class WhatsAppNotification(NotificationChannel):
    def send(self, customer, order_id, total):
        # Nueva lógica...
```

## 🎓 Aprendizajes Clave

1. **Patrones de Diseño**: No son recetas mágicas, son soluciones a problemas recurrentes
2. **SOLID**: Facilita el mantenimiento y evolución del código
3. **Refactorización**: El código limpio es un proceso iterativo
4. **Abstracción**: Las interfaces bien diseñadas son la clave de la flexibilidad

## 📝 Diagramas UML

Cada ejercicio incluye tres diagramas PlantUML:
- **c1.puml**: Diagrama de clases
- **c2.puml**: Diagrama de secuencia
- **c3.puml**: Diagrama de componentes

Para visualizar los diagramas, usa [PlantUML Online](http://www.plantuml.com/plantuml/uml/) o instala la extensión de PlantUML en VS Code.

## 🔄 Evolución del Proyecto

```
Versión 1.0 (Original)
    ↓
Análisis de problemas de diseño
    ↓
Identificación de patrones aplicables
    ↓
Refactorización con Strategy + Factory
    ↓
Versión 2.0 (Refactorizada)
```

## 🤝 Contribuciones

Este es un proyecto académico, pero las sugerencias son bienvenidas:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de uso académico.

## ✨ Autor

**Juan Pablo Gutierrez**
- GitHub: [@juanpagutierrez](https://github.com/juanpagutierrez)

---

⭐ Si este proyecto te ayudó a entender patrones de diseño, ¡dale una estrella!
