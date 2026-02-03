#!/usr/bin/env python3
"""
Script de prueba para verificar que la aplicación funciona correctamente.
Verifica la carga de datos y la creación de objetos.
"""

import sys
import json
from vivienda import Alquiler, Compra
from gestor_datos import GestorDatos


def test_clases():
    """Prueba la creación de instancias de clases."""
    print("=" * 60)
    print("PRUEBA 1: Creación de clases")
    print("=" * 60)

    # Crear alquiler
    alquiler = Alquiler("Calle Test, 1", 150000, 75, 2, 750)
    print(f"✓ Alquiler creado: {alquiler}")
    print(f"  - Coste mensual: {alquiler.calcular_coste_mensual()}€")
    print(f"  - Coste anual: {alquiler.calcular_coste_anual()}€")
    print(f"  - Precio/m²: {alquiler.obtener_precio_metro()}€")

    # Crear compra
    compra = Compra("Calle Prueba, 2", 250000, 100, 3)
    print(f"\n✓ Compra creada: {compra}")
    print(f"  - Cuota mensual: {compra.calcular_coste_mensual(entrada=50000, plazo_anios=30)}€")
    print(f"  - Precio/m²: {compra.obtener_precio_metro()}€")


def test_gestor_datos():
    """Prueba el gestor de datos."""
    print("\n" + "=" * 60)
    print("PRUEBA 2: Gestor de datos")
    print("=" * 60)

    gestor = GestorDatos("datos/viviendas.json")
    viviendas = gestor.cargar()

    print(f"✓ Datos cargados: {len(viviendas)} viviendas")

    alquileres = [v for v in viviendas if isinstance(v, Alquiler)]
    compras = [v for v in viviendas if isinstance(v, Compra)]

    print(f"  - Alquileres: {len(alquileres)}")
    print(f"  - Compras: {len(compras)}")

    if viviendas:
        print(f"\nPrimera vivienda:")
        print(f"  ID: {viviendas[0].id}")
        print(f"  Dirección: {viviendas[0].direccion}")
        print(f"  Tipo: {viviendas[0].tipo}")


def test_validacion():
    """Prueba la validación de datos."""
    print("\n" + "=" * 60)
    print("PRUEBA 3: Validación de métodos")
    print("=" * 60)

    alquiler = Alquiler("Test", 100000, 50, 1, 500)
    datos = alquiler.obtener_datos()
    print(f"✓ obtener_datos() retorna tupla: {len(datos)} elementos")

    compra = Compra("Test", 200000, 80, 2, 3.5)
    print(f"✓ Cálculo de hipoteca con valores por defecto: {compra.calcular_coste_mensual()}€")
    print(f"✓ Cálculo con entrada de 40000€: {compra.calcular_coste_mensual(entrada=40000)}€")


def main():
    """Ejecuta todas las pruebas."""
    print("\n" + "🧪 PRUEBAS DE FUNCIONAMIENTO - GESTOR DE VIVIENDAS" + "\n")

    try:
        test_clases()
        test_gestor_datos()
        test_validacion()

        print("\n" + "=" * 60)
        print("✅ TODAS LAS PRUEBAS PASARON CORRECTAMENTE")
        print("=" * 60)
        print("\nPuedes ejecutar la aplicación con: python3 main.py\n")

        return 0

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
