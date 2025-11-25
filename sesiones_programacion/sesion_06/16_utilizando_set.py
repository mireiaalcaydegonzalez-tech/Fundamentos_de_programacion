# Algunos ejemplos sobre sets
lista = ["1", 2, "3"] # son mutables
tupla = ("1", 2, "3") # no son mutables
sets = {"1", 2, "3"} # son mutables

set_from_lista = set(lista)
print(set_from_lista)
set_from_lista.add(4)
lista.append(4)
print(lista)
print(set_from_lista)

# Eliminar un elemento
set_from_lista.remove("3")
print(set_from_lista)

# Lista con duplicados
lista_con_duplicados = [1,2,2,1,3,7,4,9,3]
lista_sin_duplicados = []
for i in range(len(lista_con_duplicados)):
    if lista_con_duplicados[i] not in lista_sin_duplicados:
        lista_sin_duplicados.append(lista_con_duplicados[i])
print(lista_sin_duplicados)

# Listas sin duplicados con set
lista_sin_duplicados_set = set(lista_con_duplicados)
print(lista_sin_duplicados_set)

# Si quisiera generar directamente una lista del set podria hacer:
lista_sin_duplicados_set = list(set(lista_con_duplicados))
print(lista_sin_duplicados_set)

