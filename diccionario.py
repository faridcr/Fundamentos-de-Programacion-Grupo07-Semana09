
# Crea una lista de diccionarios para 4 estudiantes con los campos: 'nombre', 'carrera' y 'promedio'.
# Imprime el nombre y promedio de cada estudiante.
# Luego muestra el nombre del estudiante con el promedio más alto

estudiantes = [
    {"nombre": "Carlos", "carrera": "Ingeniería", "promedio": 8.5},
    {"nombre": "Ana", "carrera": "Medicina", "promedio": 9.2},
    {"nombre": "Beatriz", "carrera": "Derecho", "promedio": 7.8},
    {"nombre": "David", "carrera": "Arquitectura", "promedio": 8.9}
]

for estudiante in estudiantes:
    print(f"{estudiante['nombre']} - Promedio: {estudiante['promedio']}")

mejor_estudiante = max(estudiantes, key=lambda x: x["promedio"])
print(f"El estudiante con el promedio más alto es: {mejor_estudiante['nombre']}") 