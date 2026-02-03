# Gestor de Búsqueda de Vivienda para Jóvenes en Valencia

## Descripción

Aplicación diseñada para ayudar a jóvenes en Valencia a **gestionar su búsqueda de vivienda**, permitiendo:

- 📋 **Registrar alquileres** disponibles en el mercado
- 🏠 **Registrar opciones de compra** con cálculo automático de hipotecas
- ⚖️ **Comparar** opciones de alquiler vs compra
- 📊 **Generar reportes gráficos** para análisis de datos

## Estructura del Proyecto

```
GestionViviendas/
├── main.py              # Archivo principal para ejecutar la app
├── vivienda.py          # Clases Vivienda, Alquiler y Compra
├── gestor_datos.py      # Gestión de datos (guardado/carga JSON)
├── tab_alquiler.py      # Interfaz de gestión de alquileres
├── tab_compra.py        # Interfaz de gestión de compras
├── tab_comparativa.py   # Interfaz de comparativa
├── tab_reportes.py      # Interfaz de reportes gráficos
├── datos/
│   └── viviendas.json   # Archivo de datos persistente
└── README.md            # Este archivo
```

## Requisitos

- Python 3.7+
- tkinter (incluido en Python)
- matplotlib

## Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias** (solo matplotlib):
```bash
pip install matplotlib
```

## Uso

1. **Ejecutar la aplicación**:
```bash
python main.py
```

2. **Interfaz Principal**:
   - **Pestaña Alquileres**: Agregar, editar y eliminar viviendas en alquiler
   - **Pestaña Compras**: Agregar viviendas en venta con cálculo de hipoteca
   - **Pestaña Comparativa**: Visualizar todas las opciones registradas
   - **Pestaña Reportes**: Generar gráficas de análisis

## Características Principales

### 1. Gestión de Alquileres
- Registrar dirección, precio referencia, metros, habitaciones
- Establecer renta mensual
- Marcar disponibilidad (Disponible, Reservado, Visitado)
- Añadir notas personales

### 2. Gestión de Compras
- Registrar precio de venta
- Cálculo automático de cuota mensual de hipoteca
- Especificar entrada y plazo (años)
- Configurar tasa de interés

### 3. Comparativa
- Visualizar lado a lado alquileres vs compras
- Estadísticas de costes promedio
- Precio por metro² de cada vivienda

### 4. Reportes Gráficos
- **Distribución**: Gráfica de pastel (Alquiler vs Compra)
- **Precio/m²**: Comparativa visual de precios por metro²
- **Costes Mensuales**: Gráfica de barras con costes
- **Habitaciones**: Distribución de viviendas por número de habitaciones

## Clases Implementadas

### Vivienda (Clase Padre)
```python
Propiedades:
- id: Identificador único
- direccion: Dirección de la vivienda
- precio: Precio en euros
- metros: Metros cuadrados
- habitaciones: Número de habitaciones
- fecha_registro: Fecha de registro
- notas: Notas personales

Métodos:
- calcular_coste_mensual(): Método abstracto
- obtener_precio_metro(): Calcula €/m²
- obtener_datos(): Retorna datos como tupla
```

### Alquiler (Clase Hija)
```python
Propiedades adicionales:
- renta_mensual: Precio del alquiler mensual
- disponibilidad: Estado (Disponible, Reservado, Visitado)
- tipo: "Alquiler"

Métodos:
- calcular_coste_mensual(): Retorna renta mensual
- calcular_coste_anual(): Retorna coste anual
```

### Compra (Clase Hija)
```python
Propiedades adicionales:
- interes_anual: Tasa de interés (default 3.5%)
- plazo_anios: Plazo de la hipoteca (default 30)
- entrada: Dinero de entrada (default 0)
- tipo: "Compra"

Métodos:
- calcular_coste_mensual(entrada, plazo): Calcula cuota hipotecaria
```

## Almacenamiento de Datos

Los datos se guardan automáticamente en formato JSON (`datos/viviendas.json`):
- Al agregar/editar/eliminar una vivienda
- Permite cargar los datos al reiniciar la aplicación

## Estándares de Código

- ✅ Sigue PEP 8
- ✅ Docstrings en todas las clases y métodos
- ✅ Código modularizado en archivos separados
- ✅ Validación de entrada de datos
- ✅ Manejo de excepciones

## Notas para el Desarrollo

### Para alcanzar 80% (Requisitos mínimos)
- [x] Aplicación funcional con TkInter
- [x] Interfaz basada en pestañas
- [x] Formularios de alta/actualización/borrado
- [x] Uso de TreeView para visualización
- [x] Carga/almacenamiento de datos
- [x] Modularización en archivos
- [x] Clases Padre + 2 Hijas con 3+ propiedades y 2+ métodos
- [x] Comentarios documentados
- [x] Cumple PEP 8

### Para alcanzar 100% (Extras)
- [x] Pestaña de reportes con gráficas
- [x] Múltiples tipos de informes (4 gráficas diferentes)
- [x] Integración con matplotlib
- [x] Análisis visual de datos

## Posibles Mejoras Futuras

- Exportar reportes a PDF
- Integración con APIs de datos inmobiliarios
- Cálculo de impuestos y gastos adicionales
- Sistema de filtros avanzados
- Notificaciones de nuevas propiedades
- Geolocalización en mapas

## Autor
Sistema desarrollado con inteligencia artificial para propósitos educativos

## Licencia
Libre para uso educativo
