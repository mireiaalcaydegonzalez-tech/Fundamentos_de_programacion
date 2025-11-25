#Los datos de carla
nombre_carla = "Carla"
edad_carla = "21"
altura_carla = 1.82
dorsal_carla = 12

# Los datos de Lucia
nombre_lucia = "Lucia"
# Esto es un desproposito, por eso usamos listas

""" TRANSFORMACION CON LISTAS """
jugadora_carla = [ "Carla", "21", 1.82, 12]
jugadora_lucia = [ "Lucia" , "20", 1.85, 23]

print(jugadora_carla)

# Acceder a un elemaneto
print(f"La edad de {jugadora_carla} es {jugadora_carla}")
print(f"La edad de {jugadora_carla[0]} es {jugadora_carla[1]}")

# Posicion de campo
jugadora_carla.append ("Pivot")
print(jugadora_carla)

jugadora_carla.insert (2, "Capitana")
print(jugadora_carla)

# Eliminar la edad de Carla
jugadora_carla.remove ("21")
print(jugadora_carla)

# Eliminar la edad
jugadora_carla.pop (1)
jugadora_lucia.pop (1)
print (jugadora_carla)
print (jugadora_lucia)

#Longitud de la lista
print (f"Tenemos {len(jugadora_carla)} datos de {jugadora_carla[0]}")

