"""
Módulo que define la clase base Vivienda y sus subclases.
Gestión de propiedades para búsqueda y comparativa de viviendas en Valencia.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Vivienda(ABC):
    """
    Clase padre que representa una vivienda.
    Define propiedades y métodos comunes para todos los tipos de vivienda.
    """

    contador_id = 1

    def __init__(self, direccion, precio, metros, habitaciones):
        """
        Inicializa una vivienda con datos básicos.

        Args:
            direccion (str): Dirección de la vivienda
            precio (float): Precio en euros
            metros (float): Metros cuadrados
            habitaciones (int): Número de habitaciones
        """
        self.id = Vivienda.contador_id
        Vivienda.contador_id += 1
        self.direccion = direccion
        self.precio = precio
        self.metros = metros
        self.habitaciones = habitaciones
        self.fecha_registro = datetime.now().strftime("%d/%m/%Y")
        self.notas = ""

    @abstractmethod
    def calcular_coste_mensual(self):
        """Calcula el coste mensual de la vivienda (hipoteca o alquiler)."""
        pass

    def obtener_precio_metro(self):
        """
        Calcula el precio por metro cuadrado.

        Returns:
            float: Precio por metro cuadrado
        """
        return round(self.precio / self.metros, 2)

    def obtener_datos(self):
        """
        Retorna los datos básicos de la vivienda como tupla.

        Returns:
            tuple: Datos de la vivienda
        """
        return (
            self.id,
            self.direccion,
            self.habitaciones,
            self.metros,
            f"{self.precio}€",
            f"{self.obtener_precio_metro()}€/m²",
        )

    def __str__(self):
        return (
            f"ID: {self.id} | {self.direccion} | "
            f"{self.habitaciones} hab | {self.metros}m² | {self.precio}€"
        )


class Alquiler(Vivienda):
    """
    Clase que representa una vivienda en alquiler.
    Hereda de Vivienda e implementa cálculo de coste mensual de alquiler.
    """

    def __init__(self, direccion, precio, metros, habitaciones, renta_mensual):
        """
        Inicializa una vivienda en alquiler.

        Args:
            direccion (str): Dirección de la vivienda
            precio (float): Precio de anuncio (referencia)
            metros (float): Metros cuadrados
            habitaciones (int): Número de habitaciones
            renta_mensual (float): Renta mensual en euros
        """
        super().__init__(direccion, precio, metros, habitaciones)
        self.renta_mensual = renta_mensual
        self.disponibilidad = "Disponible"
        self.tipo = "Alquiler"

    def calcular_coste_mensual(self):
        """
        Calcula el coste mensual del alquiler.

        Returns:
            float: Renta mensual
        """
        return self.renta_mensual

    def calcular_coste_anual(self):
        """
        Calcula el coste anual del alquiler.

        Returns:
            float: Coste anual
        """
        return self.renta_mensual * 12

    def obtener_datos(self):
        """
        Retorna los datos del alquiler incluyendo renta mensual.

        Returns:
            tuple: Datos del alquiler
        """
        datos_base = super().obtener_datos()
        return datos_base + (f"{self.renta_mensual}€/mes", self.disponibilidad)


class Compra(Vivienda):
    """
    Clase que representa una vivienda en venta.
    Hereda de Vivienda e implementa cálculo de hipoteca.
    """

    def __init__(self, direccion, precio, metros, habitaciones, interes_anual=3.5):
        """
        Inicializa una vivienda en venta.

        Args:
            direccion (str): Dirección de la vivienda
            precio (float): Precio de venta en euros
            metros (float): Metros cuadrados
            habitaciones (int): Número de habitaciones
            interes_anual (float): Tasa de interés anual (default 3.5%)
        """
        super().__init__(direccion, precio, metros, habitaciones)
        self.interes_anual = interes_anual
        self.plazo_anios = 30
        self.entrada = 0
        self.tipo = "Compra"

    def calcular_coste_mensual(self, entrada=0, plazo_anios=30):
        """
        Calcula la cuota mensual de hipoteca usando fórmula estándar.

        Args:
            entrada (float): Dinero de entrada (default 0)
            plazo_anios (int): Años de plazo (default 30)

        Returns:
            float: Cuota mensual aproximada
        """
        self.entrada = entrada
        self.plazo_anios = plazo_anios

        capital = self.precio - entrada
        tasa_mensual = self.interes_anual / 100 / 12
        num_cuotas = plazo_anios * 12

        if tasa_mensual == 0:
            return round(capital / num_cuotas, 2)

        cuota = capital * (tasa_mensual * (1 + tasa_mensual) ** num_cuotas) / (
            (1 + tasa_mensual) ** num_cuotas - 1
        )
        return round(cuota, 2)

    def obtener_datos(self):
        """
        Retorna los datos de compra incluyendo interés e información hipotecaria.

        Returns:
            tuple: Datos de compra
        """
        datos_base = super().obtener_datos()
        cuota = self.calcular_coste_mensual()
        return datos_base + (f"{cuota}€/mes", f"{self.interes_anual}%")
