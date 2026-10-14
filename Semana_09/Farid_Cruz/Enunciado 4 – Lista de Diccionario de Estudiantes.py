# Ejercicio 4 - Lista de Diccionarios de Estudiantes

estudiantes = [
    {'nombre': 'Josué', 'carrera': 'Administración',         'promedio': 16},
    {'nombre': 'Kevin', 'carrera': 'Ingeniería Industrial',  'promedio': 14},
    {'nombre': 'Andy',  'carrera': 'Contabilidad',           'promedio': 18},
    {'nombre': 'Italo', 'carrera': 'Ingeniería de Sistemas', 'promedio': 15},
]

# Imprimir nombre y promedio de cada estudiante
print("=== PROMEDIOS ===")
for est in estudiantes:
    print(f"{est['nombre']}: {est['promedio']}")

# Estudiante con el promedio más alto usando max() y lambda
mejor = max(estudiantes, key=lambda e: e['promedio'])

print("-" * 25)
print(f"Promedio más alto: {mejor['nombre']} ({mejor['promedio']})")