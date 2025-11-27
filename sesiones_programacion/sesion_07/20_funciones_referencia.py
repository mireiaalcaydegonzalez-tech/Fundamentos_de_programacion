# Ejemplo modificacion parametro
# Paso por valor/ no se modifica
def modificar_numero(numero):
    numero = numero * 2

# Ejemplo con una lista
# paso por referencia
def modificar_lista(lista):
    lista.append(10)


numero_original = 5
print(f"El nuumero original es {numero_original}")
modificar_numero(numero_original)
print(f"El numero origial es {numero_original}")

# PASO POR REFERENCIA
lista_original = [1, 2, 3]
print(lista_original)
modificar_lista(lista_original)
print(lista_original)


