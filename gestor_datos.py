"""
Módulo para gestionar almacenamiento y carga de datos en JSON.
Permite persistencia de viviendas en archivo.
"""

import json
import os
from vivienda import Alquiler, Compra


class GestorDatos:
    """Gestiona la persistencia de datos de viviendas en archivo JSON."""

    def __init__(self, ruta_archivo="datos/viviendas.json"):
        """
        Inicializa el gestor de datos.

        Args:
            ruta_archivo (str): Ruta del archivo JSON
        """
        self.ruta_archivo = ruta_archivo
        self.viviendas = []
        self._asegurar_directorio()

    def _asegurar_directorio(self):
        """Crea el directorio si no existe."""
        directorio = os.path.dirname(self.ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

    def guardar(self, viviendas):
        """
        Guarda las viviendas en archivo JSON.

        Args:
            viviendas (list): Lista de viviendas a guardar
        """
        datos = []
        for v in viviendas:
            if isinstance(v, Alquiler):
                datos.append({
                    "tipo": "Alquiler",
                    "id": v.id,
                    "direccion": v.direccion,
                    "precio": v.precio,
                    "metros": v.metros,
                    "habitaciones": v.habitaciones,
                    "renta_mensual": v.renta_mensual,
                    "disponibilidad": v.disponibilidad,
                    "fecha_registro": v.fecha_registro,
                    "notas": v.notas,
                })
            elif isinstance(v, Compra):
                datos.append({
                    "tipo": "Compra",
                    "id": v.id,
                    "direccion": v.direccion,
                    "precio": v.precio,
                    "metros": v.metros,
                    "habitaciones": v.habitaciones,
                    "interes_anual": v.interes_anual,
                    "entrada": v.entrada,
                    "plazo_anios": v.plazo_anios,
                    "fecha_registro": v.fecha_registro,
                    "notas": v.notas,
                })

        try:
            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def cargar(self):
        """
        Carga las viviendas desde archivo JSON.

        Returns:
            list: Lista de viviendas cargadas
        """
        self.viviendas = []

        if not os.path.exists(self.ruta_archivo):
            return []

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)

            for item in datos:
                if item["tipo"] == "Alquiler":
                    v = Alquiler(
                        item["direccion"],
                        item["precio"],
                        item["metros"],
                        item["habitaciones"],
                        item["renta_mensual"],
                    )
                    v.id = item["id"]
                    v.disponibilidad = item.get("disponibilidad", "Disponible")
                    v.notas = item.get("notas", "")
                elif item["tipo"] == "Compra":
                    v = Compra(
                        item["direccion"],
                        item["precio"],
                        item["metros"],
                        item["habitaciones"],
                        item["interes_anual"],
                    )
                    v.id = item["id"]
                    v.entrada = item.get("entrada", 0)
                    v.plazo_anios = item.get("plazo_anios", 30)
                    v.notas = item.get("notas", "")

                self.viviendas.append(v)

            # Actualizar contador de IDs
            if self.viviendas:
                max_id = max(v.id for v in self.viviendas)
                from vivienda import Vivienda
                Vivienda.contador_id = max_id + 1

        except Exception as e:
            print(f"Error al cargar datos: {e}")

        return self.viviendas

    def obtener_vivienda_por_id(self, vivienda_id):
        """
        Obtiene una vivienda por su ID.

        Args:
            vivienda_id (int): ID de la vivienda

        Returns:
            Vivienda: Vivienda encontrada o None
        """
        for v in self.viviendas:
            if v.id == vivienda_id:
                return v
        return None
