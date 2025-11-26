# A partir de la actividad 03 "tortilla de patatas"
# Crear un pequeño script que le devuelva al ususario qué móvil
# puede comprarse en función del dinero
# el sistema operativo que prefiere (iOS o Android)
# y si la cámara es importante para él o no.

# Lista de requisistos

ios = False
android = False
precio = False
camara = False
pantalla = False
caracteristicas = []

# Preguntar al usuario
iphone = input("¿Quieres un iPhone? (s/n)")
if iphone == "s":
    caracteristicas.append("iPhone")
    ios = True
    android = False
elif iphone == "n":
    movil_android = input("¿Prefieres un móvil Android? (s/n)")
    if movil_android == "s":
        android = True
        caracteristicas.append("Android")
    else:
        caracteristicas.append("No quiere movil")
        #caracteristicas.append("No iphone")
else:
    caracteristicas.append("Respuesta no valida")
    ios = False

if android == True or ios == True:
    importe = input("¿Presupuesto mayor de 1000 euros? (s/n)")
    if importe == "s":
        precio = True
    else:
        caracteristicas.append("Precio")
    fotos = input("¿Te interesa que hagas buenas fotos? (s/n)")
    if fotos == "s":
        camara = True
    else:
        caracteristicas.append("Camara")
    plegable = input("¿Quieres que la pantalla sea plegable? (s/n)")
    if plegable == "s":
        pantalla = True
        print("Dentro de 1 año hablamos")
    #    caracteristicas.append("Plegable")
    else:
        print("En este momento es una buena elección")
        caracteristicas.append("No plegable")

    # tengo que buscar ofertas
    if ios and android and precio and camara and plegable:
        print("Eso no existe")
    else:
        print("Te recomiendo buscar ofertas por internet")
    if len(caracteristicas) == 0:
        print("¿A qué estamos jugando? Cuando domine el mundo, te buscare")
    else:
        print("Las caracteristicas del móvil a tener en cuenta son:")
        for item in caracteristicas:
            print(f"- {item}")
    #        print("- " + item)