# Generar una funcion que simule el lanzamiento de un dado de seis caras 
# y que devuelva el resultado
import random
def lanzar_dados():
    dado1 = random.randint(1, 6)
    return dado1
# Probar la funcion 
resultado = lanzar_dados()