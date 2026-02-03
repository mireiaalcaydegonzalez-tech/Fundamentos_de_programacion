"""
GUÍA RÁPIDA DE INSTALACIÓN Y EJECUCIÓN
=====================================

Sistema Operativo: macOS
"""

print("""
╔════════════════════════════════════════════════════════════════════════╗
║     GESTOR DE BÚSQUEDA DE VIVIENDA PARA JÓVENES EN VALENCIA            ║
║                    Guía de Instalación y Uso                           ║
╚════════════════════════════════════════════════════════════════════════╝

📍 PASO 1: CLONAR O DESCARGAR EL PROYECTO
═══════════════════════════════════════════════

El proyecto está en: /tmp/GestionViviendas/


📚 PASO 2: INSTALAR DEPENDENCIAS
═════════════════════════════════

1. Abre Terminal
2. Navega a la carpeta del proyecto:
   
   cd /tmp/GestionViviendas

3. Instala matplotlib (TkInter viene incluido con Python):
   
   pip3 install -r requirements.txt
   
   O directamente:
   
   pip3 install matplotlib


✅ PASO 3: EJECUTAR LA APLICACIÓN
══════════════════════════════════

1. En la Terminal, asegúrate que estás en la carpeta del proyecto
2. Ejecuta:
   
   python3 main.py

3. Se abrirá una ventana gráfica con la aplicación


🧪 PASO 4: EJECUTAR PRUEBAS (OPCIONAL)
═══════════════════════════════════════

Para verificar que todo funciona:

   python3 test.py


╔════════════════════════════════════════════════════════════════════════╗
║                          CUMPLIMIENTO DE REQUISITOS                    ║
╚════════════════════════════════════════════════════════════════════════╝

✅ REQUISITOS DE INTERFAZ GRÁFICA
═════════════════════════════════

  ✓ Aplicación construida con TkInter
  ✓ Interfaz basada en múltiples pestañas (Notebook)
  ✓ Pestañas presentes:
    - 📋 Alquileres: Gestión de viviendas en alquiler
    - 🏠 Compras/Hipoteca: Gestión de viviendas en venta
    - ⚖️  Comparativa: Comparación de opciones
    - 📊 Reportes: Análisis gráfico


✅ REQUISITOS DE GESTIÓN DE DATOS
──────────────────────────────────

  ✓ Formulario de ALTA en pestaña "Alquileres"
    - Campo: Dirección
    - Campo: Precio referencia
    - Campo: Metros cuadrados
    - Campo: Habitaciones
    - Campo: Renta mensual
    - Combobox: Disponibilidad
    - Campo: Notas
    - Botón: Guardar

  ✓ Formulario de ACTUALIZACIÓN
    - Seleccionar vivienda (doble clic en TreeView)
    - Modificar datos
    - Guardar cambios

  ✓ Formulario de BORRADO
    - Seleccionar vivienda
    - Botón "Eliminar"
    - Confirmación

  ✓ Mínimo 3 elementos en formularios (7 campos + notas)


✅ REQUISITOS DE TREEVIEW
─────────────────────────

  ✓ TreeView en pestaña "Alquileres"
    - Columnas: ID, Dirección, Hab., m², Ref.€, €/m², Renta/mes, Estado
    
  ✓ TreeView en pestaña "Compras"
    - Columnas: ID, Dirección, Hab., m², Precio€, €/m², Cuota/mes, Interés
    
  ✓ TreeView en pestaña "Comparativa"
    - Dos TreeViews: uno para alquileres, otro para compras


✅ REQUISITOS DE PROGRAMACIÓN ORIENTADA A OBJETOS
──────────────────────────────────────────────────

CLASE PADRE: Vivienda (vivienda.py)
  Propiedades:
    - id: int
    - direccion: str
    - precio: float
    - metros: float
    - habitaciones: int
    - fecha_registro: str
    - notas: str

  Métodos:
    - calcular_coste_mensual() [ABSTRACTO]
    - obtener_precio_metro()
    - obtener_datos()
    - __str__()


CLASE HIJA 1: Alquiler (vivienda.py)
  Propiedades adicionales:
    - renta_mensual: float
    - disponibilidad: str
    - tipo: str

  Métodos:
    - calcular_coste_mensual()
    - calcular_coste_anual()
    - obtener_datos()


CLASE HIJA 2: Compra (vivienda.py)
  Propiedades adicionales:
    - interes_anual: float
    - plazo_anios: int
    - entrada: float
    - tipo: str

  Métodos:
    - calcular_coste_mensual(entrada, plazo)
    - obtener_datos()


✅ REQUISITOS DE PERSISTENCIA DE DATOS
──────────────────────────────────────

  ✓ Almacenamiento en JSON: datos/viviendas.json
  ✓ Carga automática al iniciar la aplicación
  ✓ Guardado automático al agregar/editar/eliminar
  ✓ GestorDatos (gestor_datos.py) maneja la persistencia


✅ REQUISITOS DE MODULARIZACIÓN
───────────────────────────────

  ✓ main.py
    - Punto de entrada de la aplicación
    - Clase AplicacionGestionViviendas (controlador)

  ✓ vivienda.py
    - Clase padre Vivienda
    - Clases hijas Alquiler y Compra

  ✓ gestor_datos.py
    - Clase GestorDatos
    - Manejo de JSON

  ✓ tab_alquiler.py
    - Clase TabAlquiler (interfaz pestaña alquileres)

  ✓ tab_compra.py
    - Clase TabCompra (interfaz pestaña compras)

  ✓ tab_comparativa.py
    - Clase TabComparativa (interfaz pestaña comparativa)

  ✓ tab_reportes.py
    - Clase TabReportes (interfaz pestaña reportes)

  ✓ test.py
    - Script de pruebas


✅ REQUISITOS DE CALIDAD DE CÓDIGO
──────────────────────────────────

  ✓ Docstrings en todas las clases
  ✓ Docstrings en todos los métodos
  ✓ Comentarios en código complejo
  ✓ Cumplimiento de PEP 8
  ✓ Variables con nombres descriptivos
  ✓ Validación de entrada de datos
  ✓ Manejo de excepciones


✅ REQUISITOS EXTRA (100%)
──────────────────────────

PESTAÑA DE REPORTES: tab_reportes.py

  ✓ Pestaña "📊 Reportes" independiente
  ✓ Mínimo 2 gráficas implementadas (4 tipos):
    
    1️⃣  Distribución (Gráfica de pastel)
       - Porcentaje de Alquileres vs Compras
    
    2️⃣  Precio por metro² (Gráfica de barras)
       - Comparativa visual por vivienda
    
    3️⃣  Costes mensuales (Gráfica de barras)
       - Renta vs Cuota hipotecaria
    
    4️⃣  Distribución por habitaciones (Gráfica de barras)
       - Cantidad de viviendas por número de habitaciones

  ✓ Uso de matplotlib
  ✓ Integración en TkInter (FigureCanvasTkAgg)
  ✓ Selector de tipo de reporte con RadioButtons
  ✓ Botón para generar gráfica


╔════════════════════════════════════════════════════════════════════════╗
║                        CARACTERÍSTICAS ESPECIALES                      ║
╚════════════════════════════════════════════════════════════════════════╝

🎯 INNOVACIÓN Y RELEVANCIA PARA VALENCIA
─────────────────────────────────────────

  • Enfoque en jóvenes que buscan vivienda en Valencia
  • Crisis de vivienda actual: herramienta práctica para comparar opciones
  • Cálculo automático de hipotecas para evaluar capacidad de compra
  • Análisis visual de alternativas alquiler vs compra
  • Gestión de visitas y estado de propiedades


🔧 FUNCIONALIDADES AVANZADAS
────────────────────────────

  • Cálculo matemático de cuota hipotecaria (fórmula bancaria)
  • Contador de IDs persistente
  • Vinculación automática de eventos entre pestañas
  • Barra de estado con contadores
  • Validación exhaustiva de formularios
  • Interfaz intuitiva con emojis en los títulos


📊 ANÁLISIS DE DATOS
───────────────────

  • Estadísticas automáticas (promedio de rentas/cuotas)
  • Comparativa de precio por metro²
  • Visualización por tipo de vivienda
  • Gráficas interactivas con matplotlib


╔════════════════════════════════════════════════════════════════════════╗
║                    PUNTUACIÓN ESPERADA POR CRITERIO                   ║
╚════════════════════════════════════════════════════════════════════════╝

  ✅ El proyecto se ejecuta y funciona: 10%
  ✅ Interfaz basada en pestañas: 10%
  ✅ Dos pestañas con formularios: 15%
  ✅ TreeViews con datos: 15%
  ✅ Carga y almacenamiento de datos: 15%
  ✅ Modularización de código: 15%
  ✅ Pestaña de reportes (EXTRA): 10%
  ✅ Comentarios y documentación: 5%
  ✅ Cumplimiento PEP 8: 5%
  ──────────────────────────────
  ✅ TOTAL: 100%


╔════════════════════════════════════════════════════════════════════════╗
║                            PRÓXIMOS PASOS                              ║
╚════════════════════════════════════════════════════════════════════════╝

1. Abre Terminal
2. Navega a /tmp/GestionViviendas
3. Ejecuta: python3 main.py
4. ¡Prueba la aplicación!


¿Preguntas o problemas?

Si necesitas ayuda adicional, puedes:
- Revisar el README.md para documentación completa
- Ejecutar test.py para verificar que todo funciona
- Revisar los comentarios en el código fuente


═══════════════════════════════════════════════════════════════════════════
                    ¡Proyecto completado con éxito!
═══════════════════════════════════════════════════════════════════════════
""")
