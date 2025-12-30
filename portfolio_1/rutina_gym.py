"""
Programa para crear rutinas de entrenamiento teniendo en cuenta
tiempos y combinaciones realistas de grupos musculares.

Autor: Tu nombre
"""

import csv
import os
import random


CSV_FILE = "ejercicios.csv"
RUTINAS_DIR = "rutinas"

# Combinaciones lógicas
COMBINACIONES = [
    ["pecho", "espalda", "abdominales"],
    ["biceps", "triceps", "abdominales"],
    ["pierna", "abdominales"],
    ["hombro", "triceps", "abdominales"],
    ["biceps", "hombro", "abdominales"]
]


def cargar_ejercicios():
    """
    Carga los ejercicios del CSV y los agrupa por músculo.
    """
    grupos = {
        "hombro": [],
        "biceps": [],
        "triceps": [],
        "pecho": [],
        "espalda": [],
        "pierna": [],
        "abdominales": []
    }

    with open(CSV_FILE, encoding="utf-8") as file:
        lector = csv.DictReader(file)
        for fila in lector:
            grupo = fila["grupo"].lower().strip()
            nombre = fila["nombre"].strip()
            if grupo in grupos:
                grupos[grupo].append(nombre)

    return grupos


def pedir_numero(mensaje, minimo, maximo):
    """
    Pide un número entero dentro de un rango.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Introduce un valor entre {minimo} y {maximo}")
        except ValueError:
            print("Introduce un número válido")


def ejercicios_por_grupo(minutos, grupo):
    """
    Define cuántos ejercicios asignar por grupo
    según el tiempo total y el músculo.
    """

    # 45–59 minutos → 2 ejercicios para todos
    if minutos <= 59:
        return 2

    # 60–79 minutos
    elif minutos <= 79:
        if grupo == "pierna":
            return 3
        else:
            return random.randint(2, 3)

    # 80–90 minutos
    else:
        if grupo == "pierna":
            return random.randint(4, 5)
        else:
            return 3



def generar_rutina(ejercicios):
    """
    Genera la rutina semanal según la estructura fija solicitada.
    """

    dias = pedir_numero("¿Cuántos días entrenas? (3-5): ", 3, 5)
    minutos = pedir_numero("¿Minutos por día? (45-90): ", 45, 90)

    plan = {
        3: [
            ["hombro", "biceps", "triceps"],
            ["pecho", "espalda"],
            ["pierna", "abdominales"]
        ],
        4: [
            ["hombro", "espalda"],
            ["biceps", "triceps"],
            ["pecho", "abdominales"],
            ["pierna"]
        ],
        5: [
            ["pierna"],
            ["abdominales"],
            ["biceps", "triceps"],
            ["espalda", "hombro"],
            ["pecho", "abdominales"]
        ]
    }

    seleccion = plan[dias]
    rutina = {}

    for i in range(dias):
        grupos = seleccion[i]
        rutina[f"Día {i+1}"] = {}

        for grupo in grupos:
            disponibles = ejercicios[grupo]

            k = min(
                ejercicios_por_grupo(minutos, grupo),
                len(disponibles)
            )

            rutina[f"Día {i+1}"][grupo] = random.sample(disponibles, k=k)

    # Construir texto
    texto = []
    texto.append("RUTINA PERSONALIZADA SEGÚN PLAN FIJO\n")
    texto.append(f"Días por semana: {dias}")
    texto.append(f"Duración diaria aproximada: {minutos} minutos\n")

    for dia, grupos in rutina.items():
        texto.append(f"\n{dia}:")
        for grupo, lista in grupos.items():
            texto.append(f"\n {grupo.capitalize()}:")
            for ej in lista:
                texto.append(f"   - {ej}")

    return "\n".join(texto)



def guardar_rutina(texto):
    """
    Guarda la rutina en un archivo txt.
    """
    os.makedirs(RUTINAS_DIR, exist_ok=True)

    nombre = input("Nombre para la rutina: ").strip()
    ruta = os.path.join(RUTINAS_DIR, f"{nombre}.txt")

    with open(ruta, "w", encoding="utf-8") as file:
        file.write(texto)

    print(f"\nRutina guardada en {ruta}")


def listar_rutinas():
    """
    Lista rutinas guardadas.
    """
    if not os.path.exists(RUTINAS_DIR):
        print("No hay rutinas guardadas.")
        return []

    archivos = os.listdir(RUTINAS_DIR)

    if not archivos:
        print("No hay rutinas guardadas.")
        return []

    print("\nRUTINAS DISPONIBLES:")
    for i, archivo in enumerate(archivos, 1):
        print(f"{i}. {archivo}")

    return archivos


def cargar_rutina():
    """
    Muestra una rutina ya guardada.
    """
    archivos = listar_rutinas()

    if not archivos:
        return

    opcion = pedir_numero("Selecciona una rutina: ", 1, len(archivos))

    ruta = os.path.join(RUTINAS_DIR, archivos[opcion - 1])

    with open(ruta, encoding="utf-8") as file:
        print("\n" + file.read())


def menu():
    """
    Menú principal del programa.
    """

    ejercicios = cargar_ejercicios()

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Crear nueva rutina")
        print("2. Cargar rutina guardada")
        print("3. Salir")

        opcion = input("Selecciona opción: ")

        if opcion == "1":
            rutina = generar_rutina(ejercicios)
            print("\n" + rutina)
            guardar_rutina(rutina)

        elif opcion == "2":
            cargar_rutina()

        elif opcion == "3":
            print("Gracias por usar el programa 💪")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()
