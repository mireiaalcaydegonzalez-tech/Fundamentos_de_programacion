# Funcion sin parametros
def saludar():
    print("Hola ¿como estas?")
def saludar_nombre(nombre="Marta"):
    print(f"Hola {nombre}, ¿como estas?")

# Difinir una funcion que realice una suma
def suma(a,b):
    print(a+b)

def suma_return(a,b):
    print(a+b)
    return a+b


# Uso de las funciones
saludar()
suma(3,2)

resultado = suma_return(4, 20)

# Funciones con param con valor predeterminado
# saludar_nombre() ---> Error
# En cambio, si yo le asigno un valor predeterminado saludar_nombre(nombre= "Marta")
# si que es posible realizar al funcio de abajo
saludar_nombre()
saludar_nombre("Paco")

print("Fin del codigo")

