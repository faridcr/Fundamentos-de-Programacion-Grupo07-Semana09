# ---------- Ejercicio 4: lista de diccionarios ----------

estudiantes = [
    {'nombre': 'Ana',  'carrera': 'Sistemas',       'promedio': 16.5},
    {'nombre': 'Luis', 'carrera': 'Administración', 'promedio': 14.0},
    {'nombre': 'Mía',  'carrera': 'Contabilidad',   'promedio': 17.2},
    {'nombre': 'Juan', 'carrera': 'Derecho',        'promedio': 15.1},
]
for e in estudiantes:
    print(e['nombre'], e['promedio'])
 
mejor = max(estudiantes, key=lambda e: e['promedio'])
print("Promedio más alto:", mejor['nombre'])
 