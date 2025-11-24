# Variables para el calculo del IMC
peso = 50.3 # en kilogramos
altura = 1.58 # altura en m

# Calculo del IMC
imc = peso / (altura ** 2)
imc = peso / (altura *altura)
print (imc)

# Calcular el resultado
if imc < 18.5:
    print("Bajo peso")
# imc >= 18.5 and imc < 25:
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 26.9:
    print ("Peso moderado")
elif 27 <= imc < 29.9:
    print ("Sobrepeso")
elif imc >=30:
    print ("Obesidad")
else:
    print ("Error")


