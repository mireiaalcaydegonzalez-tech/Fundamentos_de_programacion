# Semaforo
# verde= 1
# amarillo = 2
# rojo = 3
verde = 1
amarillo = 2
rojo = 3

# Estado del semaforo
semaforo ="Azul"

# Control del trafico
if semaforo == verde:
    print("Esta en verde")
    print("Puedes pasar")
elif semaforo == amarillo:
    print("Esta en amarillo")
    print("Pasar con precaución")
elif semaforo == rojo:
    print("Esta en rojo")
    print("No puedes pasar")
else:
    print("El semafoto esta roto")

print("CONTINUA DESPUES DEL IF")


