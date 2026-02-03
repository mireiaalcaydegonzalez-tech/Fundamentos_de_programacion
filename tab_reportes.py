"""
Módulo para la pestaña de reportes e informes gráficos.
Genera gráficas con matplotlib sobre los datos de viviendas.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from vivienda import Alquiler, Compra


class TabReportes:
    """Interfaz para generar reportes y gráficas."""

    def __init__(self, parent, controlador):
        """
        Inicializa la pestaña de reportes.

        Args:
            parent: Widget padre
            controlador: Controlador principal de la aplicación
        """
        self.controlador = controlador
        self.frame = ttk.Frame(parent)

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Crea la interfaz de la pestaña."""
        # Frame de opciones
        frame_opciones = ttk.LabelFrame(self.frame, text="Seleccionar Reporte")
        frame_opciones.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(frame_opciones, text="Tipo de Reporte:").pack(anchor=tk.W, padx=5, pady=5)

        self.var_reporte = tk.StringVar(value="distribucion")
        reportes = [
            ("Distribución por tipo (Alquiler vs Compra)", "distribucion"),
            ("Precio por metro² (Comparativa)", "precio_metro"),
            ("Costes mensuales por vivienda", "costes_mensuales"),
            ("Distribución por habitaciones", "habitaciones"),
        ]

        for texto, valor in reportes:
            ttk.Radiobutton(
                frame_opciones,
                text=texto,
                variable=self.var_reporte,
                value=valor
            ).pack(anchor=tk.W, padx=20)

        ttk.Button(
            frame_opciones,
            text="Generar Gráfica",
            command=self._generar_grafica
        ).pack(anchor=tk.W, padx=20, pady=10)

        # Frame para la gráfica
        self.frame_grafica = ttk.LabelFrame(self.frame, text="Gráfica")
        self.frame_grafica.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def _generar_grafica(self):
        """Genera la gráfica según el tipo seleccionado."""
        tipo = self.var_reporte.get()

        # Limpiar gráfica anterior
        for widget in self.frame_grafica.winfo_children():
            widget.destroy()

        try:
            if tipo == "distribucion":
                self._grafica_distribucion()
            elif tipo == "precio_metro":
                self._grafica_precio_metro()
            elif tipo == "costes_mensuales":
                self._grafica_costes_mensuales()
            elif tipo == "habitaciones":
                self._grafica_habitaciones()
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar gráfica: {str(e)}")

    def _grafica_distribucion(self):
        """Gráfica de distribución Alquiler vs Compra."""
        alquileres = len([v for v in self.controlador.gestor_datos.viviendas if isinstance(v, Alquiler)])
        compras = len([v for v in self.controlador.gestor_datos.viviendas if isinstance(v, Compra)])

        if alquileres == 0 and compras == 0:
            messagebox.showwarning("Datos", "No hay viviendas registradas")
            return

        fig = Figure(figsize=(8, 5), dpi=100)
        ax = fig.add_subplot(111)

        labels = ["Alquileres", "Compras"]
        sizes = [alquileres, compras]
        colors = ["#FF9999", "#66B2FF"]

        ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
        ax.set_title("Distribución: Alquileres vs Compras")

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _grafica_precio_metro(self):
        """Gráfica de precio por metro² por vivienda."""
        viviendas = self.controlador.gestor_datos.viviendas

        if not viviendas:
            messagebox.showwarning("Datos", "No hay viviendas registradas")
            return

        etiquetas = [f"{v.direccion[:20]}..." for v in viviendas]
        precios = [v.obtener_precio_metro() for v in viviendas]

        fig = Figure(figsize=(10, 5), dpi=100)
        ax = fig.add_subplot(111)

        colores = ["#FF9999" if isinstance(v, Alquiler) else "#66B2FF" for v in viviendas]
        ax.bar(range(len(etiquetas)), precios, color=colores)
        ax.set_xlabel("Vivienda")
        ax.set_ylabel("€ por m²")
        ax.set_title("Precio por metro² por Vivienda")
        ax.set_xticks(range(len(etiquetas)))
        ax.set_xticklabels(etiquetas, rotation=45, ha="right")

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _grafica_costes_mensuales(self):
        """Gráfica de costes mensuales."""
        alquileres = [v for v in self.controlador.gestor_datos.viviendas if isinstance(v, Alquiler)]
        compras = [v for v in self.controlador.gestor_datos.viviendas if isinstance(v, Compra)]

        if not alquileres and not compras:
            messagebox.showwarning("Datos", "No hay viviendas registradas")
            return

        fig = Figure(figsize=(10, 5), dpi=100)
        ax = fig.add_subplot(111)

        x_pos = 0
        etiquetas = []
        costes = []
        colores = []

        for v in alquileres:
            etiquetas.append(f"{v.direccion[:15]}...")
            costes.append(v.calcular_coste_mensual())
            colores.append("#FF9999")
            x_pos += 1

        for v in compras:
            etiquetas.append(f"{v.direccion[:15]}...")
            costes.append(v.calcular_coste_mensual())
            colores.append("#66B2FF")
            x_pos += 1

        ax.bar(range(len(etiquetas)), costes, color=colores)
        ax.set_xlabel("Vivienda")
        ax.set_ylabel("€ mensuales")
        ax.set_title("Costes Mensuales por Vivienda")
        ax.set_xticks(range(len(etiquetas)))
        ax.set_xticklabels(etiquetas, rotation=45, ha="right")

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _grafica_habitaciones(self):
        """Gráfica de distribución por habitaciones."""
        viviendas = self.controlador.gestor_datos.viviendas

        if not viviendas:
            messagebox.showwarning("Datos", "No hay viviendas registradas")
            return

        # Contar por habitaciones
        distribucion = {}
        for v in viviendas:
            hab = v.habitaciones
            if hab not in distribucion:
                distribucion[hab] = 0
            distribucion[hab] += 1

        habitaciones = sorted(distribucion.keys())
        cantidades = [distribucion[h] for h in habitaciones]

        fig = Figure(figsize=(8, 5), dpi=100)
        ax = fig.add_subplot(111)

        ax.bar([str(h) for h in habitaciones], cantidades, color="#90EE90")
        ax.set_xlabel("Número de Habitaciones")
        ax.set_ylabel("Cantidad de Viviendas")
        ax.set_title("Distribución por Número de Habitaciones")

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def actualizar(self):
        """Actualiza la pestaña (llamada desde el controlador)."""
        pass
