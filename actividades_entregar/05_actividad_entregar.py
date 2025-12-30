# Script: Plantilla de jugadores con más características
# Ahora incluye: edad, equipo y guardado en archivo

jugadores = []   # Lista que almacenará diccionarios con los datos de cada jugador

while True:
    nombre = input("Introduce el nombre del jugador (o 'salir' para terminar): ")

    if nombre.lower() == "salir":
        break

    posicion = input(f"Introduce la posición de {nombre} (base, alero, pivot...): ")

    # Validamos la edad
    while True:
        try:
            edad = int(input(f"Introduce la edad de {nombre}: "))
            if edad <= 0:
                print("La edad debe ser mayor que 0.")
                continue
            break
        except ValueError:
            print("Debes introducir un número válido para la edad.")

    dorsal = input(f"Introduce el dorsal de {nombre}: ")

    equipo = input(f"Introduce el equipo de {nombre}: ")

    # Diccionario con los datos del jugador
    jugador = {
        'nombre': nombre,
        'posicion': posicion,
        'edad': edad,
        'dorsal': dorsal,
        'equipo': equipo
    }

    # Lo añadimos a la lista
    jugadores.append(jugador)

# Mostrar plantilla final en pantalla
print(f"\n---- PLANTILLA FINAL ({len(jugadores)} jugadores) ----")
for jugador in jugadores:
    print(f"Nombre: {jugador['nombre']}, Posición: {jugador['posicion']}, Edad: {jugador['edad']}, "
          f"Dorsal: {jugador['dorsal']}, Equipo: {jugador['equipo']}")

