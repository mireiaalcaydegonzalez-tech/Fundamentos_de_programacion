# Lista para comprarse un telefono nuevo
poco_dinero = False
dinero = False
mucho_dinero = False
iOS = False
Android = False
camara = False
no_camara = False

# Preguntar al usuario por el dinero
tienes_poco_dinero = input("¿Dispones de entre 0 y 150 euros? (s/n)")
if tienes_poco_dinero == "s":
    poco_dinero = True
tienes_dinero = input ("¿Dispones de entre 150 y 400 euros? (s/n)")
elif tienes_dinero == "s":
    dinero = True
tienes_mucho_dinero = input("¿Dispones de más de 400 euros? (s/n)")
else:
mucho_dinero = True

# Puedes elegir
if poco_dinero:
    print("Me tendré que conformar")
elif dinero or mucho_dinero:
    print("Puedo comprar un buen movil")
