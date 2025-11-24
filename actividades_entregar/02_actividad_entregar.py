# Variables para el calculo de la nota media
Evaluacion_1 = 8.5
Evaluacion_2 = 4.5
Evaluacion_3 = 9

# Calculo de la nota media
Media_final = (Evaluacion_1+Evaluacion_2+Evaluacion_3)/3
print(Media_final)

# Calcular el resultado
if Media_final <= 4.9:
     print("Suspenso")
elif 5.0 <= Media_final <= 6.9:
    print("Aprobado")
elif 7.0 <= Media_final <= 8.9:
    print("Notable")
elif 9.0 <= Media_final <=10:
    print("Sobresaliente")
else:
    print("Error")