# Listas vacias de jugadores/anotaciones
lista_anotaciones = [] #preguntar al usuario
lista_jugadores = []
max_anotacion = 0
nombre_maxima_anotacion = ""

for jugador in range(3):
        # Pedir al usuario el jugador y las anotaciones
        nombre_jugador = input(f"Introduce el nombre del jugador numero {jugador}")
        anotacion_jugador = int(input(f"Dame la anotacion del jugador num {jugador}")) # Esta es una linea mucho mas larga que sobre pasa

        # Andir a las listas
        lista_anotaciones.append(anotacion_jugador)
        lista_jugadores.append(nombre_jugador)

        # Calcular el maximo anotador
        if anotacion_jugador > max_anotacion:
            maxima_anotacion = anotacion_jugador
            nombre_maxima_anotacion = nombre_jugador

# Resultados finales
for jugador in range(3):
        print(f"Jugador {lista_jugadores[jugador]} ha anotado {lista_anotaciones[jugador]} ptos.")

print(f"La maxima anotacion ha sido {maxima_anotacion}")
print(f"Del jugador {nombre_maxima_anotacion}")
