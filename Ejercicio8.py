
nombres = ["Ana", "Luis", "Maria", "Pedro"]

notas = {
    "Python": [18, 15, 20, 14],
    "Matematica": [16, 17, 19, 13],
    "Base de Datos": [17, 14, 18, 16]
}

def promedio_materia(materia):
    return sum(notas[materia]) / len(notas[materia])


def mejor_estudiante(materia):
    mayor = max(notas[materia])
    posicion = notas[materia].index(mayor)
    return nombres[posicion]


def reporte_general():
    resultados = []

    for i in range(len(nombres)):
        total = 0

        for materia in notas:
            total += notas[materia][i]

        promedio = total / len(notas)

        resultados.append({
            "nombre": nombres[i],
            "promedio": promedio
        })

    resultados.sort(key=lambda dato: dato["promedio"], reverse=True)

    print("\nREPORTE GENERAL")

    for estudiante in resultados:
        print(estudiante["nombre"], "- Promedio:", estudiante["promedio"])


for materia in notas:
    print("\nMateria:", materia)
    print("Promedio:", promedio_materia(materia))
    print("Mejor estudiante:", mejor_estudiante(materia))

reporte_general()
