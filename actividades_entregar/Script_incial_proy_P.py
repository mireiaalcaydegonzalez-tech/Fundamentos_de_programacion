"""
Script base para generar rutinas de gimnasio.
Versión sencilla para empezar el proyecto.

Autor: (tu nombre)
"""

import os


RUTINAS_DIR = "rutinas"


def mostrar_menu():
    """Muestra el menú principal en pantalla."""
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Crear nueva rutina")
    print("2. Cargar rutina guardada")
    print("3. Salir")


def pedir_numero(mensaje, minimo, maximo):
    """Pide un número entero dentro de un rango."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Introduce un valor entre {minimo} y {maximo}")
        except ValueError:
            print("Introduce un número válido")


def crear_rutina():
    """Crea una rutina básica a partir de los datos del usuario."""

    print("\n--- CREAR NUEVA RUTINA ---")

    dias = pedir_numero(
        "¿Cuántos días entrenas por semana? (3-5): ",
        3,
        5
    )

    minutos = pedir_numero(
        "¿Cuántos minutos por día? (45-90): ",
        45,
        90
    )

    grupos = [
        "Hombro",
        "Bíceps",
        "Tríceps",
        "Pecho",
        "Espalda",
        "Pierna",
        "Abdominales"
    ]

    # reparto simple de grupos por día
    rutina = {f"Día {i+1}": [] for i in range(dias)}

    i = 0
    for grupo in grupos:
        rutina[f"Día {(i % dias) + 1}"].append(grupo)
        i += 1

    texto = []
    texto.append("RUTINA SEMANAL DE GIMNASIO\n")
    texto.append(f"Días por semana: {dias}")
    texto.append(f"Tiempo por día aproximado: {minutos} minutos\n")

    for dia, musculos in rutina.items():
        texto.append(f"\n{dia}:")
        for m in musculos:
            texto.append(f" - {m}")

    resultado = "\n".join(texto)

    print("\nRutina generada correctamente:")
    print(resultado)

    guardar_rutina(resultado)


def guardar_rutina(texto):
    """Guarda la rutina en un archivo txt dentro de /rutinas."""

    os.makedirs(RUTINAS_DIR, exist_ok=True)

    nombre = input("\nNombre para la rutina: ").strip()
    ruta = os.path.join(RUTINAS_DIR, f"{nombre}.txt")

    with open(ruta, "w", encoding="utf-8") as fichero:
        fichero.write(texto)

    print(f"\nRutina guardada en: {ruta}")


def listar_rutinas():
    """Devuelve y muestra las rutinas guardadas disponibles."""

    if not os.path.exists(RUTINAS_DIR):
        print("\nNo hay rutinas guardadas.")
        return []

    archivos = os.listdir(RUTINAS_DIR)

    if not archivos:
        print("\nNo hay rutinas guardadas.")
        return []

    print("\nRUTINAS DISPONIBLES:")
    for i, archivo in enumerate(archivos, 1):
        print(f"{i}. {archivo}")

    return archivos


def cargar_rutina():
    """Permite seleccionar y mostrar una rutina ya guardada."""

    archivos = listar_rutinas()

    if not archivos:
        return

    opcion = pedir_numero(
        "\nSelecciona el número de rutina: ",
        1,
        len(archivos)
    )

    ruta = os.path.join(RUTINAS_DIR, archivos[opcion - 1])

    with open(ruta, "r", encoding="utf-8") as fichero:
        contenido = fichero.read()

    print("\n--- RUTINA CARGADA ---")
    print(contenido)


def main():
    """Controla el flujo principal del programa."""

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            crear_rutina()
        elif opcion == "2":
            cargar_rutina()
        elif opcion == "3":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
