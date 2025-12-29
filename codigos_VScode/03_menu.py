def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*45)
    print("           GESTOR DE LISTA DE COMPRA")
    print("="*45)
    print("1. Añadir producto")
    print("2. Ver lista de compra")
    print("3. Eliminar producto")
    print("4. Guardar lista y salir")
    print("="*45)

def añadir_producto(lista):
    """Añade un producto a la lista"""
    nombre = input("\n¿Qué producto deseas añadir?: ").strip()
    
    if not nombre:
        print("El nombre del producto no puede estar vacío.")
        return
    
    try:
        cantidad = int(input(f"¿Cuántas unidades de {nombre}?: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            return
        
        lista.append({"producto": nombre, "cantidad": cantidad})
        print(f"✓ {nombre} ({cantidad} unidades) añadido a la lista.")
    except ValueError:
        print("Error: Debes introducir un número válido.")

def ver_lista(lista):
    """Muestra la lista de compra actual"""
    if not lista:
        print("\n⚠ La lista está vacía.")
        return
    
    print("\n" + "-"*45)
    print("PRODUCTOS EN TU LISTA:")
    print("-"*45)
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item['producto']:<30} Cantidad: {item['cantidad']}")
    print("-"*45)

def eliminar_producto(lista):
    """Elimina un producto de la lista"""
    if not lista:
        print("\n⚠ La lista está vacía.")
        return
    
    ver_lista(lista)
    
    try:
        numero = int(input("\n¿Qué producto deseas eliminar? (número): "))
        if 1 <= numero <= len(lista):
            producto_eliminado = lista.pop(numero - 1)
            print(f"✓ {producto_eliminado['producto']} eliminado de la lista.")
        else:
            print("Error: Número de producto no válido.")
    except ValueError:
        print("Error: Debes introducir un número válido.")

def guardar_lista(lista):
    """Guarda la lista en un archivo txt"""
    nombre_archivo = "lista_compra.txt"
    
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("="*45 + "\n")
            archivo.write("           LISTA DE LA COMPRA\n")
            archivo.write("="*45 + "\n\n")
            
            if lista:
                for i, item in enumerate(lista, 1):
                    archivo.write(f"{i}. {item['producto']:<30} Cantidad: {item['cantidad']}\n")
            else:
                archivo.write("La lista está vacía.\n")
            
            archivo.write("\n" + "="*45 + "\n")
        
        print(f"\n✓ Lista guardada correctamente en '{nombre_archivo}'")
    except IOError as error:
        print(f"\n✗ Error al guardar el archivo: {error}")

def main():
    """Función principal que controla la aplicación"""
    lista_compra = []
    
    print("\n¡Bienvenido al gestor de lista de compra!")
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            añadir_producto(lista_compra)
        elif opcion == "2":
            ver_lista(lista_compra)
        elif opcion == "3":
            eliminar_producto(lista_compra)
        elif opcion == "4":
            guardar_lista(lista_compra)
            print("\n¡Hasta pronto!")
            break
        else:
            print("✗ Opción no válida. Por favor, selecciona 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()