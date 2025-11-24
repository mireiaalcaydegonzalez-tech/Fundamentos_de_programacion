"""
Lista de la compra para hacer una tortilla de papatas
"""

# Lista vacia de la compra
lista_compra = [ ]

# ¿ Que nos falta?
hay_patatas = input(" ¿Tienes patatas [s/n]?")
if hay_patatas.lower() == "n":
        lista_compra.append("patatas")

hay_huevos = input(" ¿Tienes huevos [s/n]?")
if hay_huevos.lower() == "n":
        lista_compra.append("huevos")


# Puedes hacerlo mas compacto (no recomendable)
if input(" ¿Tienes sal [s/n]?").lower() == "n":
        lista_compra.append("sal")

if input(" ¿Tienes aceite [s/n]?").lower() == "n":
        lista_compra.append("aceite")

# Tengo que ir al supermercado
if len(lista_compra) == 0:
    print ("No tengo que ir al supermercado")
else:
    print ("Si tengo que ir al supermercado")
    print(lista_compra)

# Forma dos de resolucion
if len(lista_compra) >= 1:
    print ("Si tengo que ir al supermercado")
    print (lista_compra)
else:
    print ( "No tengo que ir al supermercado")