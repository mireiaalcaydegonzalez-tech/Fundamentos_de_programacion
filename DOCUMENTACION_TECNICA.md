# DOCUMENTACIÓN TÉCNICA - Gestor de Búsqueda de Vivienda

## Índice
1. [Arquitectura General](#arquitectura-general)
2. [Descripción de Módulos](#descripción-de-módulos)
3. [Modelos de Datos](#modelos-de-datos)
4. [Flujo de Aplicación](#flujo-de-aplicación)
5. [Características Técnicas](#características-técnicas)

## Arquitectura General

### Patrón MVC
La aplicación sigue un patrón **Modelo-Vista-Controlador**:

```
┌─────────────────────────────────────────────────┐
│        VISTA (TkInter Tabs)                     │
│  ┌──────────────┬──────────────────────────┐   │
│  │ TabAlquiler  │ TabCompra   │ TabComp... │   │
│  └──────────────┴──────────────────────────┘   │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│  CONTROLADOR (AplicacionGestionViviendas)       │
│  - Gestiona eventos                             │
│  - Coordina vistas y modelos                    │
│  - Maneja actualización de pestañas             │
└──────────────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│  MODELO (Vivienda, Alquiler, Compra)            │
│  ┌────────────┐                                 │
│  │ Vivienda   │ (Clase Padre)                   │
│  └────────────┘                                 │
│        ▲  ▲                                      │
│        │  └─────────────────────┐               │
│        │                        ▼               │
│  ┌──────────┐            ┌─────────────┐       │
│  │ Alquiler │            │   Compra    │       │
│  └──────────┘            └─────────────┘       │
└─────────────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│  PERSISTENCIA (GestorDatos)                     │
│  - Lee/Escribe JSON                             │
│  - Maneja viviendas.json                        │
└─────────────────────────────────────────────────┘
```

## Descripción de Módulos

### 1. `main.py` - Punto de Entrada

**Responsabilidades:**
- Inicializar aplicación TkInter
- Crear ventana principal
- Instanciar controlador (AplicacionGestionViviendas)
- Crear notebook con todas las pestañas

**Clase Principal:**
```python
class AplicacionGestionViviendas:
    def __init__(self, ventana_root)
    def _crear_interfaz()
    def _on_tab_changed(event)
    def _actualizar_estado()
```

### 2. `vivienda.py` - Modelo de Datos

**Jerarquía de Clases:**

#### Vivienda (Clase Abstracta Padre)
```python
Propiedades:
  - id: int (contador automático)
  - direccion: str
  - precio: float
  - metros: float
  - habitaciones: int
  - fecha_registro: str (auto)
  - notas: str

Métodos:
  + calcular_coste_mensual() → float [ABSTRACTO]
  + obtener_precio_metro() → float
  + obtener_datos() → tuple
  + __str__() → str
```

#### Alquiler (Subclase)
```python
Hereda de: Vivienda

Propiedades Adicionales:
  - renta_mensual: float
  - disponibilidad: str
  - tipo: str = "Alquiler"

Métodos Override:
  + calcular_coste_mensual() → float [retorna renta_mensual]
  + calcular_coste_anual() → float
  + obtener_datos() → tuple [extendida]
```

#### Compra (Subclase)
```python
Hereda de: Vivienda

Propiedades Adicionales:
  - interes_anual: float (default 3.5%)
  - plazo_anios: int (default 30)
  - entrada: float (default 0)
  - tipo: str = "Compra"

Métodos Override:
  + calcular_coste_mensual(entrada=0, plazo_anios=30) → float
    [Fórmula: C = P * (i*(1+i)^n) / ((1+i)^n - 1)]
  + obtener_datos() → tuple [extendida]
```

### 3. `gestor_datos.py` - Persistencia

**Clase: GestorDatos**
```python
Responsabilidad: Manejar toda la persistencia de datos en JSON

Propiedades:
  - ruta_archivo: str
  - viviendas: list[Vivienda]

Métodos:
  + __init__(ruta_archivo: str)
  + cargar() → list[Vivienda]
  + guardar(viviendas: list[Vivienda])
  + obtener_vivienda_por_id(vivienda_id: int) → Vivienda | None
  - _asegurar_directorio() [privado]
```

**Formato JSON:**
```json
[
  {
    "tipo": "Alquiler",
    "id": 1,
    "direccion": "...",
    "precio": 150000,
    "metros": 75,
    "habitaciones": 2,
    "renta_mensual": 750,
    "disponibilidad": "Disponible",
    "fecha_registro": "01/02/2026",
    "notas": "..."
  }
]
```

### 4. `tab_alquiler.py` - Interfaz de Alquileres

**Clase: TabAlquiler**
```python
Responsabilidad: Interfaz para gestionar alquileres

Frame Principal:
  ├─ LabelFrame "Formulario de Alquiler"
  │  ├─ Entry: dirección, precio, metros, habitaciones
  │  ├─ Entry: renta_mensual
  │  ├─ Combobox: disponibilidad (Disponible/Reservado/Visitado)
  │  ├─ Text: notas
  │  └─ Botones: Guardar, Limpiar
  │
  ├─ LabelFrame "Viviendas en Alquiler"
  │  └─ Treeview: (ID, Dirección, Hab., m², Ref.€, €/m², Renta/mes, Estado)
  │
  └─ Botones: Editar, Eliminar

Métodos:
  + __init__(parent, controlador)
  + _crear_interfaz()
  + _guardar() → Agrega o actualiza alquiler
  + _editar() → Carga datos en formulario
  + _eliminar() → Elimina alquiler
  + _limpiar() → Resetea formulario
  + _actualizar_tree() → Refresca TreeView
  + actualizar() → Llamada desde controlador
```

### 5. `tab_compra.py` - Interfaz de Compras

**Clase: TabCompra**
```python
Similar a TabAlquiler pero para gestión de compras

Formulario Adicional:
  ├─ Entry: Interés Anual (%)
  ├─ Entry: Entrada (€)
  ├─ Entry: Plazo (años)
  └─ Label: Cuota mensual (calculada)

TreeView Adicional:
  └─ Columnas: (ID, Dirección, Hab., m², Precio€, €/m², Cuota/mes, Interés%)

Métodos Especiales:
  + _calcular() → Actualiza cuota mensual en tiempo real
```

### 6. `tab_comparativa.py` - Comparativa

**Clase: TabComparativa**
```python
Responsabilidad: Mostrar comparativa lado a lado

Elementos:
  ├─ Text: Información y estadísticas
  ├─ TreeView Alquileres:
  │  └─ Columnas: (ID, Dirección, Hab., m², €/m², Renta/mes, Coste Anual)
  │
  └─ TreeView Compras:
     └─ Columnas: (ID, Dirección, Hab., m², €/m², Cuota/mes, Interés)

Estadísticas Automáticas:
  - Cantidad de alquileres/compras
  - Promedio de renta mensual
  - Promedio de cuota hipotecaria
```

### 7. `tab_reportes.py` - Reportes Gráficos

**Clase: TabReportes**
```python
Responsabilidad: Generar gráficas con matplotlib

Tipos de Gráficas:
  1. Distribución (Pastel)
     - Alquileres vs Compras
  
  2. Precio por m² (Barras)
     - Comparativa por vivienda
  
  3. Costes Mensuales (Barras)
     - Renta vs Cuota por vivienda
  
  4. Habitaciones (Barras)
     - Cantidad de viviendas por número de habitaciones

Métodos:
  + _generar_grafica() → Selecciona tipo y genera
  + _grafica_distribucion()
  + _grafica_precio_metro()
  + _grafica_costes_mensuales()
  + _grafica_habitaciones()
```

## Modelos de Datos

### Estructura de Vivienda (JSON)

```json
{
  "tipo": "Alquiler|Compra",
  "id": integer,
  "direccion": string,
  "precio": float,
  "metros": float,
  "habitaciones": integer,
  "fecha_registro": "DD/MM/YYYY",
  "notas": string,
  
  // Si tipo = "Alquiler"
  "renta_mensual": float,
  "disponibilidad": "Disponible|Reservado|Visitado",
  
  // Si tipo = "Compra"
  "interes_anual": float,
  "entrada": float,
  "plazo_anios": integer
}
```

## Flujo de Aplicación

### Inicio
```
1. python3 main.py
   ↓
2. Crear ventana TkInter
   ↓
3. Instanciar AplicacionGestionViviendas
   ↓
4. GestorDatos.cargar() - Lee viviendas.json
   ↓
5. Crear Notebook con 4 pestañas
   ↓
6. TabAlquiler.actualizar() - Llena TreeView
   ↓
7. Esperar interacción usuario
```

### Agregar Vivienda
```
Usuario ingresa datos en formulario
   ↓
Clic en "Guardar"
   ↓
_guardar() valida entrada
   ↓
Crea objeto Alquiler/Compra
   ↓
Agrega a GestorDatos.viviendas[]
   ↓
GestorDatos.guardar() - Escribe JSON
   ↓
_actualizar_tree() - Refresca interfaz
   ↓
Mostrar mensaje "Éxito"
```

### Cambiar Pestaña
```
Usuario hace clic en pestaña
   ↓
Evento <<NotebookTabChanged>>
   ↓
_on_tab_changed() identifica pestaña
   ↓
Llama actualizar() en pestaña
   ↓
_actualizar_comparativa() / _actualizar_tree()
   ↓
Refresca datos en TreeView/Gráficas
```

## Características Técnicas

### Validación de Datos
- Campos numéricos (precio, metros, habitaciones): `float()` / `int()`
- Campos requeridos: validación de strings no vacíos
- Try-except para errores de conversión
- Mensajes informativos al usuario

### Cálculo de Hipoteca
```python
Fórmula de cuota mensual:
C = P × (i×(1+i)^n) / ((1+i)^n - 1)

Donde:
  C = Cuota mensual
  P = Principal (precio - entrada)
  i = Tasa mensual (interés_anual / 100 / 12)
  n = Número de cuotas (plazo_anios × 12)
```

### Persistencia
- Guardado automático en JSON después de cada cambio
- Carga automática al iniciar la app
- IDs persistentes (no se resetean)

### Interfaz Gráfica
- Componentes TkInter: Frame, LabelFrame, Entry, Combobox, Button, Text, Treeview
- Matplotlib FigureCanvasTkAgg para gráficas integradas
- Emojis en títulos para mejor visualización
- Scrollbars automáticas en TreeViews

### Estándares de Código
- **PEP 8**: Indentación 4 espacios, nombres en snake_case
- **Docstrings**: Google-style en todas las clases y métodos
- **Comentarios**: Explicaciones en código complejo
- **Modularización**: Responsabilidad única por módulo

## Relaciones entre Módulos

```
main.py
  ├─ importa AplicacionGestionViviendas
  │   ├─ importa GestorDatos
  │   ├─ importa TabAlquiler
  │   ├─ importa TabCompra
  │   ├─ importa TabComparativa
  │   └─ importa TabReportes
  │
  └─ TabAlquiler, TabCompra, TabComparativa, TabReportes
      ├─ importan Vivienda, Alquiler, Compra
      └─ usan controlador.gestor_datos
```

## Puntos de Extensión Futura

1. **Base de datos**: Reemplazar JSON con SQLite
2. **API**: Conectar con portales de vivienda (Idealista, Fotocasa)
3. **Exportación**: PDF, Excel, reportes por email
4. **Filtros avanzados**: Por precio, zona, antigüedad
5. **Geolocalización**: Integración con Google Maps
6. **Notificaciones**: Alertas de nuevas propiedades
7. **Cálculos avanzados**: Gastos de hipoteca, impuestos, seguros

---
*Documentación generada para propósitos educativos*
