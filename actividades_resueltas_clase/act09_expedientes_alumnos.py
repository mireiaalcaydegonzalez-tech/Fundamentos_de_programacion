# Generar una lista vacía de alumnos
alumnos = []


# Pregunta al profesor por el nombre
#calf en ciencias, humanidades, arte

while True:
    nombre = input("Introduce el nombre del alumno ( o 'salir' para finalizar): ")
    if nombre.lower() == "salir":
        break
    calif_ciencias = float(input(f"Introduce la calificacion en ciencias de {nombre}: "))
    if calif_ciencias < 5.0:
        print("Suspendido")
    elif 5.0 <= calif_ciencias <= 8.9:
        print("Aprobado")
    elif 9.0 <= calif_ciencias <= 10:
        print("Matricula de honor")
    else:
        print("Error")
    calif_humanidades = float(input(f"Introduce la calificacion en humanidades de {nombre}: "))
    if calif_humanidades < 5.0:
        print("Suspendido")
    elif 5.0 <= calif_humanidades <= 8.9:
        print("Aprobado")
    elif 9.0 <= calif_humanidades <= 10:
        print("Matricula de honor")
    else:
        print("Error")
    calif_arte = float(input(f"Introduce la calificacion en arte de {nombre}: "))
    if calif_arte < 5.0:
        print("Suspendido")
    elif 5.0 <= calif_arte <= 8.9:
        print("Aprobado")
    elif 9.0 <= calif_arte <= 10:
        print("Matricula de honor")
    else:
        print("Error")
    alumno = {
        'Nombre': nombre,
        'calif_ciencias': calif_ciencias,
        'calif_humanidades': calif_humanidades,
        'calif_arte': calif_arte,
    }

    alumnos.append(alumno)


# Mostrar los  expedientes de todos los alumnos y su expediente
print(f"---LISTA DE {len(alumnos)} ALUMNOS---")
for alumno in alumnos:
    print(f"Nombre: {alumno['Nombre']}, Ciencias: {alumno['calif_ciencias']}, Humanidades: {alumno['calif_humanidades']},"
          f" Arte: {alumno['calif_arte']}")


# Cositas a corregir ahora mismo: si da error lo incluye en la lista



