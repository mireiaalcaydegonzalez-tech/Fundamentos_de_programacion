# Suma
def suma(a, b, pa = 1, pb = 1): # En este caso si que seria interesante definir los valores de pa y pb
    return pa * a + pb * b


# Resta
def resta(a, b):
    return a - b


# Multiplicacion
def multiplica(a, b):
    return a * b


# Division
def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    return result


# Interfaz
def interfaz():
    print("Selecciona la operacion")
    print("1 . Sumar")
    print("2 . Restar")
    print("3 . Multiplicar")
    print("4 . Dividir")
    print("------------")
    print("0 . Salir")


# Bucle infinito
while True:
    interfaz()

    # Pedir opcion
    opcion = int(input(" Introduce que operacion quieres reaizar [0,1,2,3,4]: "))

    if opcion == 0:
        break

    elif 0 < opcion < 5:
        try:
            numero1 = int(input("Introduce el primer numero: "))
            numero2 = int(input("Introduce el segundo numero: "))
        except ValueError:
            print("No has introducido un numero")
            continue

        # Realizo el cálculo
        try:
            if opcion == 1:
                print(f"La suma de los dos numeros es {suma(numero1, numero2)}")
            elif opcion == 2:
                print(f"La resta de los dos numeros es {resta(numero1, numero2)}")
            elif opcion == 3:
                 print(f"La multiplicacion de los dos numeros es {multiplica(numero1, numero2)}")
            elif opcion == 4:
                print(f"La division de los dos numeros es {div(numero1, numero2)}")
        except ZeroDivisionError:
            print("Existe un error")    # Esto al estar introducido previamente no va a dar error
            # por tanto no se ejecuta
        except TypeError:
            print("Existe un error en la introduccion")
    else:
        print("La opcion no es valida")

# Fin del bucle
print("Muchas gracias por utilizar mi calculadora")
