# Actividad: precios supermercado

productos = []
precios = []

while True:
    nombre = input("Introduce el nombre del producto (o 'salir' para finalizar): ")

    if nombre.lower() == "salir":
        break

    try:
        precio = float(input(f"Introduce el precio de {nombre}: "))
    except ValueError:
        print("⚠ Debes introducir un número válido para el precio.")
        continue

    if precio < 0:
        print("⚠ El precio no puede ser negativo.")
        continue

    productos.append(nombre)
    precios.append(precio)

# Al terminar, comprobamos que haya datos
if precios:
    print("\n--- RESUMEN DE LA COMPRA ---")
    print(f"Precio máximo: {max(precios)} €")
    print(f"Precio mínimo: {min(precios)} €")
    print(f"Total gastado: {sum(precios)} €")
else:
    print("No se introdujo ningún producto.")
