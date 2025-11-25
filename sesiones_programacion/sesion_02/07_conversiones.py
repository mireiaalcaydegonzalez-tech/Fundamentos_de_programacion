# Conversiones de números
a = 1
b = 12.3
ponderacion = 2
peso = 50.5
edad = "32"
separador = "-"

# Conversion  implicita
num_convertido = a + b
print(num_convertido)

print(separador*10)


# Conversion explicita
edad_doblada = ponderacion * int(edad)
print(edad_doblada)
print(ponderacion * int(edad))

# Conversiones explicitas
print(float(peso))
print(int(float(peso)))
print(int(float(edad)))

