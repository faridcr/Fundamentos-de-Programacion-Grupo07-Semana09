"""
EJERCICIO 8: Sistema de calificaciones con estructuras combinadas
Objetivo: almacenar notas por materia, calcular promedios, encontrar al mejor
estudiante de cada materia y ordenar un reporte por promedio general.
"""

nombres = ["Ana", "Luis", "María", "Carlos"]

# Cada materia tiene una lista de notas. La posición corresponde a nombres.
calificaciones = {
    "Matemática": [18, 15, 20, 14],
    "Comunicación": [17, 19, 18, 16],
    "Ciencia": [16, 14, 19, 18]
}

print("PROMEDIO POR MATERIA")
for materia, notas in calificaciones.items():
    promedio_materia = sum(notas) / len(notas)
    print(f"{materia}: {promedio_materia:.2f}")

    nota_maxima = max(notas)
    mejores = [
        nombres[i] for i, nota in enumerate(notas)
        if nota == nota_maxima
    ]
    print(f"  Mejor estudiante: {', '.join(mejores)} ({nota_maxima})")

# Calcular el promedio general de cada estudiante entre todas las materias.
reporte = []
for i, nombre in enumerate(nombres):
    notas_estudiante = [notas[i] for notas in calificaciones.values()]
    promedio_general = sum(notas_estudiante) / len(notas_estudiante)
    reporte.append({"nombre": nombre, "promedio_general": promedio_general})

reporte_ordenado = sorted(
    reporte, key=lambda estudiante: estudiante["promedio_general"], reverse=True
)

print("\nREPORTE GENERAL (de mayor a menor)")
for estudiante in reporte_ordenado:
    print(
        f"{estudiante['nombre']}: "
        f"{estudiante['promedio_general']:.2f}"
    )
