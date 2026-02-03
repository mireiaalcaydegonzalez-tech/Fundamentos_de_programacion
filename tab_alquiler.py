"""
Módulo para la pestaña de gestión de alquileres.
Permite agregar, editar y eliminar viviendas en alquiler.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from vivienda import Alquiler


class TabAlquiler:
    """Interfaz para la gestión de viviendas en alquiler."""

    def __init__(self, parent, controlador):
        """
        Inicializa la pestaña de alquiler.

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
        self.var_renta = tk.StringVar()
        self.var_disponibilidad = tk.StringVar()
        self.var_notas = tk.StringVar()

        self.id_edicion = None

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Crea la interfaz de la pestaña."""
        # Sección del formulario
        frame_formulario = ttk.LabelFrame(self.frame, text="Formulario de Alquiler")
        frame_formulario.pack(fill=tk.BOTH, padx=10, pady=10)

        campos = [
            ("Dirección:", self.var_direccion),
            ("Precio Referencia (€):", self.var_precio),
            ("Metros²:", self.var_metros),
            ("Habitaciones:", self.var_habitaciones),
            ("Renta Mensual (€):", self.var_renta),
        ]

        for label_text, variable in campos:
            ttk.Label(frame_formulario, text=label_text).pack(anchor=tk.W, padx=5)
            ttk.Entry(frame_formulario, textvariable=variable).pack(fill=tk.X, padx=5, pady=2)

        ttk.Label(frame_formulario, text="Disponibilidad:").pack(anchor=tk.W, padx=5)
        ttk.Combobox(
            frame_formulario,
            textvariable=self.var_disponibilidad,
            values=["Disponible", "Reservado", "Visitado"],
            state="readonly"
        ).pack(fill=tk.X, padx=5, pady=2)

        ttk.Label(frame_formulario, text="Notas:").pack(anchor=tk.W, padx=5)
        text_notas = tk.Text(frame_formulario, height=3, width=50)
        text_notas.pack(fill=tk.X, padx=5, pady=2)
        self.text_notas = text_notas

        # Botones de acción
        frame_botones = ttk.Frame(frame_formulario)
        frame_botones.pack(fill=tk.X, padx=5, pady=10)

        ttk.Button(frame_botones, text="Guardar", command=self._guardar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self._limpiar).pack(side=tk.LEFT, padx=5)

        # TreeView
        frame_tree = ttk.LabelFrame(self.frame, text="Viviendas en Alquiler")
        frame_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            frame_tree,
            columns=("ID", "Dirección", "Hab.", "m²", "Ref.€", "€/m²", "Renta/mes", "Estado"),
            height=8,
        )
        self.tree.heading("#0", text="")
        self.tree.column("#0", width=0, stretch=tk.NO)

        columnas_info = [
            ("ID", 50),
            ("Dirección", 200),
            ("Hab.", 50),
            ("m²", 60),
            ("Ref.€", 80),
            ("€/m²", 80),
            ("Renta/mes", 100),
            ("Estado", 100),
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

    def _guardar(self):
        """Guarda o actualiza un alquiler."""
        try:
            direccion = self.var_direccion.get().strip()
            precio = float(self.var_precio.get())
            metros = float(self.var_metros.get())
            habitaciones = int(self.var_habitaciones.get())
            renta = float(self.var_renta.get())

            if not direccion:
                messagebox.showwarning("Validación", "Ingrese una dirección")
                return

            notas = self.text_notas.get("1.0", tk.END).strip()

            if self.id_edicion:
                # Actualizar
                vivienda = self.controlador.gestor_datos.obtener_vivienda_por_id(self.id_edicion)
                if vivienda and isinstance(vivienda, Alquiler):
                    vivienda.direccion = direccion
                    vivienda.precio = precio
                    vivienda.metros = metros
                    vivienda.habitaciones = habitaciones
                    vivienda.renta_mensual = renta
                    vivienda.disponibilidad = self.var_disponibilidad.get()
                    vivienda.notas = notas
                    messagebox.showinfo("Éxito", "Alquiler actualizado")
                    self.id_edicion = None
            else:
                # Crear nuevo
                alquiler = Alquiler(direccion, precio, metros, habitaciones, renta)
                alquiler.disponibilidad = self.var_disponibilidad.get()
                alquiler.notas = notas
                self.controlador.gestor_datos.viviendas.append(alquiler)
                messagebox.showinfo("Éxito", "Alquiler agregado")

            self.controlador.gestor_datos.guardar(self.controlador.gestor_datos.viviendas)
            self._limpiar()
            self._actualizar_tree()

        except ValueError:
            messagebox.showerror("Error", "Verifica que los valores numéricos sean correctos")

    def _editar(self):
        """Edita un alquiler seleccionado."""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Selecciona un alquiler para editar")
            return

        item = self.tree.item(seleccion[0])
        vivienda_id = int(item["values"][0])

        vivienda = self.controlador.gestor_datos.obtener_vivienda_por_id(vivienda_id)
        if vivienda:
            self.id_edicion = vivienda_id
            self.var_direccion.set(vivienda.direccion)
            self.var_precio.set(str(vivienda.precio))
            self.var_metros.set(str(vivienda.metros))
            self.var_habitaciones.set(str(vivienda.habitaciones))
            self.var_renta.set(str(vivienda.renta_mensual))
            self.var_disponibilidad.set(vivienda.disponibilidad)
            self.text_notas.delete("1.0", tk.END)
            self.text_notas.insert("1.0", vivienda.notas)

    def _eliminar(self):
        """Elimina un alquiler seleccionado."""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Selecciona un alquiler para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Deseas eliminar este alquiler?"):
            item = self.tree.item(seleccion[0])
            vivienda_id = int(item["values"][0])

            self.controlador.gestor_datos.viviendas = [
                v for v in self.controlador.gestor_datos.viviendas if v.id != vivienda_id
            ]
            self.controlador.gestor_datos.guardar(self.controlador.gestor_datos.viviendas)
            self._actualizar_tree()
            messagebox.showinfo("Éxito", "Alquiler eliminado")

    def _limpiar(self):
        """Limpia el formulario."""
        self.var_direccion.set("")
        self.var_precio.set("")
        self.var_metros.set("")
        self.var_habitaciones.set("")
        self.var_renta.set("")
        self.var_disponibilidad.set("Disponible")
        self.text_notas.delete("1.0", tk.END)
        self.id_edicion = None

    def _actualizar_tree(self):
        """Actualiza el TreeView con datos de alquileres."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for v in self.controlador.gestor_datos.viviendas:
            if isinstance(v, Alquiler):
                datos = v.obtener_datos()
                self.tree.insert("", tk.END, values=datos)

    def actualizar(self):
        """Actualiza la pestaña (llamada desde el controlador)."""
        self._actualizar_tree()
