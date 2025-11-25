# A partir de la actividad 2 "IMC y clasificación"
# Crear un pequeño script que clasifique las notas de un estudiante
# según la siguiente escala:
# 0-4.9: Suspenso
# 5.0-6.9: Aprobado
# 7.0-8.9: Notable
# 9.0-10: Sobresaliente
notas_luis = {
 "Lengua": 8,
 "Matemática": 7,
 "Programación": 10,
 "Cálculo": 3
}
print("--- clasificación de Notas de Luis ---")

for materia, nota in notas_luis.items():
     if nota >= 9.0 :
        clasificacion= "Sobresaliente"
     elif nota >= 7.0:
        clasificacion = "Notable"
     elif nota >= 5.0:
        clasificacion = "Aprobado"
     elif nota >= 0.0:
        clasificacion = "Suspenso"
     else:
        clasificacion = "Error (Nota inválida)"

     print(f"{materia} ({nota}): **{clasificacion}**")