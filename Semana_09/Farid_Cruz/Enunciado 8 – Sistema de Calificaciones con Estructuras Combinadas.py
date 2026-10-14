# Ejercicio 8 - Sistema de Calificaciones con Estructuras Combinadas

# Arreglo paralelo: la posición i de 'nombres' corresponde a la posición i
# de cada lista de notas dentro del diccionario.
nombres = ['Josué', 'Kevin', 'Andy', 'Italo']

# Diccionario de listas: clave = materia, valor = lista de notas
notas = {
    'Matemática':   [16, 14, 18, 15],
    'Programación': [17, 13, 19, 18],
    'Física':       [12, 15, 14, 16],
}


def promedio_materia(notas, materia):
    """Promedio de notas de una materia."""
    return sum(notas[materia]) / len(notas[materia])


def mejor_estudiante(nombres, notas, materia):
    """Devuelve (nombre, nota) del estudiante con la nota más alta en la materia."""
    lista = notas[materia]
    mejor = 0
    for i in range(len(lista)):
        if lista[i] > lista[mejor]:
            mejor = i
    return nombres[mejor], lista[mejor]


def reporte_general(nombres, notas):
    """Lista de diccionarios con el promedio general de cada estudiante,
    ordenada de mayor a menor."""
    reporte = []
    for i in range(len(nombres)):
        total = 0
        for materia in notas:
            total += notas[materia][i]
        reporte.append({'nombre': nombres[i], 'promedio': total / len(notas)})

    reporte.sort(key=lambda r: r['promedio'], reverse=True)
    return reporte


# ----- Resultados -----
print("=== PROMEDIO POR MATERIA ===")
for materia in notas:
    print(f"{materia}: {promedio_materia(notas, materia):.2f}")

print("\n=== MEJOR ESTUDIANTE POR MATERIA ===")
for materia in notas:
    nombre, nota = mejor_estudiante(nombres, notas, materia)
    print(f"{materia}: {nombre} ({nota})")

print("\n=== REPORTE GENERAL (mayor a menor) ===")
for posicion, r in enumerate(reporte_general(nombres, notas), 1):
    print(f"{posicion}° {r['nombre']}: {r['promedio']:.2f}")