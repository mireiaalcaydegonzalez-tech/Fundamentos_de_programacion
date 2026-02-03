"""
Módulo para la pestaña de comparativa de viviendas.
Permite comparar diferentes opciones de alquiler vs compra.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from vivienda import Alquiler, Compra


class TabComparativa:
    """Interfaz para comparar viviendas."""

    def __init__(self, parent, controlador):
        """
        Inicializa la pestaña de comparativa.

        Args:
            parent: Widget padre
            controlador: Controlador principal de la aplicación
        """
        self.controlador = controlador
        self.frame = ttk.Frame(parent)

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Crea la interfaz de la pestaña."""
        # Frame superior con instrucciones
        frame_info = ttk.LabelFrame(self.frame, text="Comparativa de Viviendas")
        frame_info.pack(fill=tk.BOTH, padx=10, pady=10)

        info_text = tk.Text(frame_info, height=3, width=80, state=tk.DISABLED)
        info_text.pack(fill=tk.X, padx=5, pady=5)
        self.text_info = info_text

        # TreeView de Alquileres
        frame_alquileres = ttk.LabelFrame(self.frame, text="Alquileres")
        frame_alquileres.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree_alquileres = ttk.Treeview(
            frame_alquileres,
            columns=("ID", "Dirección", "Hab.", "m²", "€/m²", "Renta/mes", "Coste Anual"),
            height=5,
        )
        self.tree_alquileres.heading("#0", text="")
        self.tree_alquileres.column("#0", width=0, stretch=tk.NO)

        columnas = [
            ("ID", 50),
            ("Dirección", 250),
            ("Hab.", 50),
            ("m²", 60),
            ("€/m²", 80),
            ("Renta/mes", 100),
            ("Coste Anual", 100),
        ]

        for col, ancho in columnas:
            self.tree_alquileres.heading(col, text=col)
            self.tree_alquileres.column(col, width=ancho)

        scroll_alquiler = ttk.Scrollbar(frame_alquileres, orient=tk.VERTICAL, command=self.tree_alquileres.yview)
        self.tree_alquileres.configure(yscroll=scroll_alquiler.set)

        self.tree_alquileres.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_alquiler.pack(side=tk.RIGHT, fill=tk.Y)

        # TreeView de Compras
        frame_compras = ttk.LabelFrame(self.frame, text="Compras/Hipotecas")
        frame_compras.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree_compras = ttk.Treeview(
            frame_compras,
            columns=("ID", "Dirección", "Hab.", "m²", "€/m²", "Cuota/mes", "Interés"),
            height=5,
        )
        self.tree_compras.heading("#0", text="")
        self.tree_compras.column("#0", width=0, stretch=tk.NO)

        columnas_compra = [
            ("ID", 50),
            ("Dirección", 250),
            ("Hab.", 50),
            ("m²", 60),
            ("€/m²", 80),
            ("Cuota/mes", 100),
            ("Interés", 80),
        ]

        for col, ancho in columnas_compra:
            self.tree_compras.heading(col, text=col)
            self.tree_compras.column(col, width=ancho)

        scroll_compra = ttk.Scrollbar(frame_compras, orient=tk.VERTICAL, command=self.tree_compras.yview)
        self.tree_compras.configure(yscroll=scroll_compra.set)

        self.tree_compras.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_compra.pack(side=tk.RIGHT, fill=tk.Y)

    def _actualizar_comparativa(self):
        """Actualiza los datos de comparativa."""
        # Limpiar
        for item in self.tree_alquileres.get_children():
            self.tree_alquileres.delete(item)
        for item in self.tree_compras.get_children():
            self.tree_compras.delete(item)

        # Actualizar alquileres
        alquileres = [v for v in self.controlador.gestor_datos.viviendas if isinstance(v, Alquiler)]
        compras = [v for v in self.controlador.gestor_datos.viviendas if isinstance(v, Compra)]

        for v in alquileres:
            self.tree_alquileres.insert(
                "",
                tk.END,
                values=(
                    v.id,
                    v.direccion,
                    v.habitaciones,
                    v.metros,
                    f"{v.obtener_precio_metro()}€",
                    f"{v.renta_mensual}€",
                    f"{v.calcular_coste_anual()}€",
                ),
            )

        # Actualizar compras
        for v in compras:
            self.tree_compras.insert(
                "",
                tk.END,
                values=(
                    v.id,
                    v.direccion,
                    v.habitaciones,
                    v.metros,
                    f"{v.obtener_precio_metro()}€",
                    f"{v.calcular_coste_mensual()}€",
                    f"{v.interes_anual}%",
                ),
            )

        # Actualizar información
        self.text_info.config(state=tk.NORMAL)
        self.text_info.delete("1.0", tk.END)

        if alquileres and compras:
            renta_promedio = sum(v.renta_mensual for v in alquileres) / len(alquileres)
            cuota_promedio = sum(v.calcular_coste_mensual() for v in compras) / len(compras)

            info = f"Total Alquileres: {len(alquileres)} | Promedio Renta: {renta_promedio:.2f}€/mes\n"
            info += f"Total Compras: {len(compras)} | Promedio Cuota: {cuota_promedio:.2f}€/mes"
        elif alquileres:
            renta_promedio = sum(v.renta_mensual for v in alquileres) / len(alquileres)
            info = f"Total Alquileres: {len(alquileres)} | Promedio Renta: {renta_promedio:.2f}€/mes"
        elif compras:
            cuota_promedio = sum(v.calcular_coste_mensual() for v in compras) / len(compras)
            info = f"Total Compras: {len(compras)} | Promedio Cuota: {cuota_promedio:.2f}€/mes"
        else:
            info = "No hay viviendas registradas"

        self.text_info.insert("1.0", info)
        self.text_info.config(state=tk.DISABLED)

    def actualizar(self):
        """Actualiza la pestaña (llamada desde el controlador)."""
        self._actualizar_comparativa()
