# Que movil cuadra mejor contigo

dinero = input("¿Cuánto dinero tienes? (poco / medio / mucho): ").lower()
so = input("¿Qué sistema operativo prefieres? (ios / android): ").lower()
camara = input("¿Te importa mucho la cámara? (s/n): ").lower()

# Lógica de decisión
if dinero == "poco":
    if so == "android":
        print("Te recomiendo un móvil Android económico (por ejemplo un Redmi A).")
    else:
        print("Con poco dinero no es posible comprar un iPhone.")
elif dinero == "medio":
    if so == "android":
        if camara == "s":
            print("Te recomiendo un Pixel 6a.")
        else:
            print("Te recomiendo un Samsung gama media.")
    else:
        print("Te recomiendo un iPhone 13.")
elif dinero == "mucho":
    if so == "android":
        if camara == "s":
            print("Te recomiendo un Samsung S23 o Pixel 8.")
        else:
            print("Te recomiendo un Android gama alta.")
    else:
        print("Te recomiendo un iPhone 14 o superior.")
else:
    print("No he entendido tu respuesta sobre el dinero.")
