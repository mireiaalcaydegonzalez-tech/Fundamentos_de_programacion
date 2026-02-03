"""
Aplicación principal de Gestión de Búsqueda de Vivienda para Jóvenes en Valencia.

Sistema completo con interfaz gráfica TkInter para gestionar búsqueda de viviendas
en alquiler o compra, comparar opciones y generar reportes.

Autor: Sistema Inteligente
Fecha: 2026
"""

import tkinter as tk
from tkinter import ttk
from gestor_datos import GestorDatos
from tab_alquiler import TabAlquiler
from tab_compra import TabCompra
from tab_comparativa import TabComparativa
from tab_reportes import TabReportes


class AplicacionGestionViviendas:
    """Controlador principal de la aplicación."""

    def __init__(self, ventana_root):
        """
        Inicializa la aplicación principal.

        Args:
            ventana_root: Ventana raíz de TkInter
        """
        self.root = ventana_root
        self.root.title("Gestor de Búsqueda de Vivienda - Valencia")
        self.root.geometry("1200x700")

        # Inicializar gestor de datos
        self.gestor_datos = GestorDatos("datos/viviendas.json")
        self.gestor_datos.cargar()

        # Crear interfaz
        self._crear_interfaz()

    def _crear_interfaz(self):
        """Crea la interfaz principal con pestañas."""
        # Frame principal
        frame_principal = ttk.Frame(self.root)
        frame_principal.pack(fill=tk.BOTH, expand=True)

        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(frame_principal)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Crear pestañas
        self.tab_alquiler = TabAlquiler(self.notebook, self)
        self.notebook.add(self.tab_alquiler.frame, text="📋 Alquileres")

        self.tab_compra = TabCompra(self.notebook, self)
        self.notebook.add(self.tab_compra.frame, text="🏠 Compras/Hipoteca")

        self.tab_comparativa = TabComparativa(self.notebook, self)
        self.notebook.add(self.tab_comparativa.frame, text="⚖️ Comparativa")

        self.tab_reportes = TabReportes(self.notebook, self)
        self.notebook.add(self.tab_reportes.frame, text="📊 Reportes")

        # Cargar datos iniciales en las pestañas
        self.tab_alquiler.actualizar()
        self.tab_compra.actualizar()
        self.tab_comparativa.actualizar()

        # Vincular cambio de pestaña
        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_changed)

        # Barra de estado
        self.frame_estado = ttk.Frame(self.root)
        self.frame_estado.pack(fill=tk.X, padx=5, pady=5)

        self.label_estado = ttk.Label(
            self.frame_estado,
            text="Listo",
            relief=tk.SUNKEN
        )
        self.label_estado.pack(fill=tk.X)

        self._actualizar_estado()

    def _on_tab_changed(self, event):
        """Actualiza la pestaña activa."""
        pestaña_activa = self.notebook.select()

        if pestaña_activa == self.tab_alquiler.frame.winfo_id():
            self.tab_alquiler.actualizar()
        elif pestaña_activa == self.tab_compra.frame.winfo_id():
            self.tab_compra.actualizar()
        elif pestaña_activa == self.tab_comparativa.frame.winfo_id():
            self.tab_comparativa.actualizar()

        self._actualizar_estado()

    def _actualizar_estado(self):
        """Actualiza la barra de estado."""
        alquileres = len([v for v in self.gestor_datos.viviendas
                         if v.tipo == "Alquiler"])
        compras = len([v for v in self.gestor_datos.viviendas
                      if v.tipo == "Compra"])

        mensaje = f"Alquileres: {alquileres} | Compras: {compras} | Total: {alquileres + compras}"
        self.label_estado.config(text=mensaje)


def main():
    """Función principal para ejecutar la aplicación."""
    root = tk.Tk()
    app = AplicacionGestionViviendas(root)
    root.mainloop()


if __name__ == "__main__":
    main()
