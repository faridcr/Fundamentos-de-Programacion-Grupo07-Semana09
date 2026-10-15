
estudiantes = [
    {"nombre": "Ana", "carrera": "Sistemas", "promedio": 18},
    {"nombre": "Luis", "carrera": "Industrial", "promedio": 15},
    {"nombre": "Maria", "carrera": "Sistemas", "promedio": 19},
    {"nombre": "Pedro", "carrera": "Civil", "promedio": 16}
]

mayor = estudiantes[0]

for estudiante in estudiantes:
    print(estudiante["nombre"], "- Promedio:", estudiante["promedio"])

    if estudiante["promedio"] > mayor["promedio"]:
        mayor = estudiante

print("\nEstudiante con mayor promedio:")
print(mayor["nombre"], "-", mayor["promedio"])
