"""
Programa calculo imc preguntando al usuario
"""

#Pedir el peso y la altura
print("Introduce tu peso en Kg")
peso = input()
print(peso)
# como es un string y debemos convertirlo podemos hacerlo directamente de la siguiente manera:
print("Introduce tu peso en Kg")
peso = float(input())
#peso_num = float(peso)

altura = float(input("Introduce tu altura en m"))

# Calculo del IMC
IMC = peso / (altura **2)
print(IMC)