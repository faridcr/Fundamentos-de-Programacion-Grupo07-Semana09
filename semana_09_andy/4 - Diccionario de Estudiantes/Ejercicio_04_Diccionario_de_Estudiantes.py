"""
EJERCICIO 4: Lista de diccionarios de estudiantes
Objetivo: guardar nombre, carrera y promedio de cuatro estudiantes,
mostrar sus promedios y encontrar el promedio más alto.
"""

estudiantes = [
    {"nombre": "Ana", "carrera": "Ingeniería", "promedio": 17.5},
    {"nombre": "Luis", "carrera": "Administración", "promedio": 15.8},
    {"nombre": "María", "carrera": "Contabilidad", "promedio": 18.2},
    {"nombre": "Carlos", "carrera": "Ingeniería", "promedio": 16.4}
]

print("REPORTE DE ESTUDIANTES")
for estudiante in estudiantes:
    print(
        f"Nombre: {estudiante['nombre']} | "
        f"Promedio: {estudiante['promedio']:.2f}"
    )

# max() encuentra el diccionario cuyo promedio es mayor.
mejor_estudiante = max(estudiantes, key=lambda estudiante: estudiante["promedio"])

print("\nEstudiante con el promedio más alto:")
print(f"{mejor_estudiante['nombre']} - {mejor_estudiante['promedio']:.2f}")
