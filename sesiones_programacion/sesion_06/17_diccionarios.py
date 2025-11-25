# Creación de un nuevo diccionario
registro_sara = {
    "Nombre": "Sara",
    "Edad": 27,
    "Id": 1003546
    }

registro_mireia = dict(
    [
        ('Nombre', 'Mireia'),
        ('Edad', 23),
        ("Id", 1002345)
    ]
)
print(registro_sara)
print(registro_mireia)

# Imprimir un valor
print(registro_mireia["Nombre"])

# Imprimir los valores de un diccionario
for clave in registro_mireia:
    print(registro_mireia[clave])
for value in registro_mireia.values():
    print(value)
    
# Imprimir todo
registro_mireia["Altura"] = 180
for clave,valor in registro_mireia.items():
    print(f"{clave} = {valor}")