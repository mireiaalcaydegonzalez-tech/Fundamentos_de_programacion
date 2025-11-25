# Preguntar al usuario por su nombre y DNI
# Almacenamos en listas diferentes
nombres = []
dnis = []

#Bucle interaccion con el usuario
while True:
    nombre = input("Introduce tu nombre ( o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    dni = input("introduce tu DNI: ")
    nombres.append(nombre)
    dnis.append(dni)

# Imprimir los usuarios y los dni que se han registrado
for i in range(len(nombres)):
    print(f"Nombre: {nombres[i]} con DNI: {dnis[i]}")

# Otra forma de imprimir lo mismo sin range
# i = 0
#for nombre in nombres:
#   print(f"Nombre: {nombre} con DNI: {dnis[i]}")
#    i +=1

# Calcular el numero de usuarios diferentes en un dia
usuarios_diferentes = set(dnis)
print(f"El dia de hoy han habido {len(usuarios_diferentes)} usuarios diferentes en el gimnasio" )


