"""
Módulo para la pestaña de gestión de compras de vivienda.
Permite agregar, editar y eliminar viviendas en venta con cálculo de hipotecas.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from vivienda import Compra


class TabCompra:
    """Interfaz para la gestión de viviendas en venta."""

    def __init__(self, parent, controlador):
        """
        Inicializa la pestaña de compra.

        Args:
            parent: Widget padre
            controlador: Controlador principal de la aplicación
        """
        self.controlador = controlador
        self.frame = ttk.Frame(parent)

        # Variables del formulario
        self.var_direccion = tk.StringVar()
        self.var_precio = tk.StringVar()
        self.var_metros = tk.StringVar()
        self.var_habitaciones = tk.StringVar()
        self.var_interes = tk.StringVar(value="3.5")
        self.var_entrada = tk.StringVar(value="0")
        self.var_plazo = tk.StringVar(value="30")
        self.var_notas = tk.StringVar()

        self.id_edicion = None

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Crea la interfaz de la pestaña."""
        # Sección del formulario
        frame_formulario = ttk.LabelFrame(self.frame, text="Formulario de Compra")
        frame_formulario.pack(fill=tk.BOTH, padx=10, pady=10)

        campos = [
            ("Dirección:", self.var_direccion),
            ("Precio (€):", self.var_precio),
            ("Metros²:", self.var_metros),
            ("Habitaciones:", self.var_habitaciones),
            ("Interés Anual (%):", self.var_interes),
            ("Entrada (€):", self.var_entrada),
            ("Plazo (años):", self.var_plazo),
        ]

        for label_text, variable in campos:
            ttk.Label(frame_formulario, text=label_text).pack(anchor=tk.W, padx=5)
            ttk.Entry(frame_formulario, textvariable=variable).pack(fill=tk.X, padx=5, pady=2)

        ttk.Label(frame_formulario, text="Notas:").pack(anchor=tk.W, padx=5)
        text_notas = tk.Text(frame_formulario, height=3, width=50)
        text_notas.pack(fill=tk.X, padx=5, pady=2)
        self.text_notas = text_notas

        # Frame para cuota calculada
        frame_calculo = ttk.Frame(frame_formulario)
        frame_calculo.pack(fill=tk.X, padx=5, pady=10)

        self.label_cuota = ttk.Label(frame_calculo, text="Cuota mensual: --€", font=("Arial", 10, "bold"))
        self.label_cuota.pack(anchor=tk.W)

        # Botones de acción
        frame_botones = ttk.Frame(frame_formulario)
        frame_botones.pack(fill=tk.X, padx=5, pady=10)

        ttk.Button(frame_botones, text="Calcular", command=self._calcular).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Guardar", command=self._guardar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self._limpiar).pack(side=tk.LEFT, padx=5)

        # TreeView
        frame_tree = ttk.LabelFrame(self.frame, text="Viviendas en Venta")
        frame_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            frame_tree,
            columns=("ID", "Dirección", "Hab.", "m²", "Precio€", "€/m²", "Cuota/mes", "Interés"),
            height=8,
        )
        self.tree.heading("#0", text="")
        self.tree.column("#0", width=0, stretch=tk.NO)

        columnas_info = [
            ("ID", 50),
            ("Dirección", 200),
            ("Hab.", 50),
            ("m²", 60),
            ("Precio€", 90),
            ("€/m²", 80),
            ("Cuota/mes", 100),
            ("Interés", 80),
        ]

        for col, ancho in columnas_info:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=ancho)

        scrollbar = ttk.Scrollbar(frame_tree, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Botones de gestión
        frame_gestion = ttk.Frame(self.frame)
        frame_gestion.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(frame_gestion, text="Editar", command=self._editar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_gestion, text="Eliminar", command=self._eliminar).pack(side=tk.LEFT, padx=5)

        self.tree.bind("<Double-1>", lambda e: self._editar())

    def _calcular(self):
        """Calcula la cuota mensual de la hipoteca."""
        try:
            precio = float(self.var_precio.get())
            entrada = float(self.var_entrada.get())
            plazo = int(self.var_plazo.get())
            interes = float(self.var_interes.get())

            compra = Compra("", precio, 0, 0, interes)
            cuota = compra.calcular_coste_mensual(entrada, plazo)

            self.label_cuota.config(text=f"Cuota mensual: {cuota}€")
        except ValueError:
            messagebox.showerror("Error", "Verifica que los valores numéricos sean correctos")

    def _guardar(self):
        """Guarda o actualiza una compra."""
        try:
            direccion = self.var_direccion.get().strip()
            precio = float(self.var_precio.get())
            metros = float(self.var_metros.get())
            habitaciones = int(self.var_habitaciones.get())
            interes = float(self.var_interes.get())
            entrada = float(self.var_entrada.get())
            plazo = int(self.var_plazo.get())

            if not direccion:
                messagebox.showwarning("Validación", "Ingrese una dirección")
                return

            notas = self.text_notas.get("1.0", tk.END).strip()

            if self.id_edicion:
                # Actualizar
                vivienda = self.controlador.gestor_datos.obtener_vivienda_por_id(self.id_edicion)
                if vivienda and isinstance(vivienda, Compra):
                    vivienda.direccion = direccion
                    vivienda.precio = precio
                    vivienda.metros = metros
                    vivienda.habitaciones = habitaciones
                    vivienda.interes_anual = interes
                    vivienda.entrada = entrada
                    vivienda.plazo_anios = plazo
                    vivienda.notas = notas
                    messagebox.showinfo("Éxito", "Compra actualizada")
                    self.id_edicion = None
            else:
                # Crear nuevo
                compra = Compra(direccion, precio, metros, habitaciones, interes)
                compra.entrada = entrada
                compra.plazo_anios = plazo
                compra.notas = notas
                self.controlador.gestor_datos.viviendas.append(compra)
                messagebox.showinfo("Éxito", "Compra agregada")

            self.controlador.gestor_datos.guardar(self.controlador.gestor_datos.viviendas)
            self._limpiar()
            self._actualizar_tree()

        except ValueError:
            messagebox.showerror("Error", "Verifica que los valores numéricos sean correctos")

    def _editar(self):
        """Edita una compra seleccionada."""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Selecciona una compra para editar")
            return

        item = self.tree.item(seleccion[0])
        vivienda_id = int(item["values"][0])

        vivienda = self.controlador.gestor_datos.obtener_vivienda_por_id(vivienda_id)
        if vivienda and isinstance(vivienda, Compra):
            self.id_edicion = vivienda_id
            self.var_direccion.set(vivienda.direccion)
            self.var_precio.set(str(vivienda.precio))
            self.var_metros.set(str(vivienda.metros))
            self.var_habitaciones.set(str(vivienda.habitaciones))
            self.var_interes.set(str(vivienda.interes_anual))
            self.var_entrada.set(str(vivienda.entrada))
            self.var_plazo.set(str(vivienda.plazo_anios))
            self.text_notas.delete("1.0", tk.END)
            self.text_notas.insert("1.0", vivienda.notas)
            self._calcular()

    def _eliminar(self):
        """Elimina una compra seleccionada."""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Selecciona una compra para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Deseas eliminar esta compra?"):
            item = self.tree.item(seleccion[0])
            vivienda_id = int(item["values"][0])

            self.controlador.gestor_datos.viviendas = [
                v for v in self.controlador.gestor_datos.viviendas if v.id != vivienda_id
            ]
            self.controlador.gestor_datos.guardar(self.controlador.gestor_datos.viviendas)
            self._actualizar_tree()
            messagebox.showinfo("Éxito", "Compra eliminada")

    def _limpiar(self):
        """Limpia el formulario."""
        self.var_direccion.set("")
        self.var_precio.set("")
        self.var_metros.set("")
        self.var_habitaciones.set("")
        self.var_interes.set("3.5")
        self.var_entrada.set("0")
        self.var_plazo.set("30")
        self.text_notas.delete("1.0", tk.END)
        self.label_cuota.config(text="Cuota mensual: --€")
        self.id_edicion = None

    def _actualizar_tree(self):
        """Actualiza el TreeView con datos de compras."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for v in self.controlador.gestor_datos.viviendas:
            if isinstance(v, Compra):
                datos = v.obtener_datos()
                self.tree.insert("", tk.END, values=datos)

    def actualizar(self):
        """Actualiza la pestaña (llamada desde el controlador)."""
        self._actualizar_tree()
