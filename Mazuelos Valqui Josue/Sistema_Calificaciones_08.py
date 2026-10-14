# ---------- Ejercicio 8: sistema de calificaciones ----------

alumnos = ['Ana', 'Luis', 'Mía']
notas = {
    'Matemática':   [16, 12, 18],
    'Programación': [19, 15, 17],
}
 
def promedio_materia():
    for materia, lista in notas.items():
        print(materia, "promedio:", round(sum(lista) / len(lista), 2))
 
def mejor_alumno():
    for materia, lista in notas.items():
        i = lista.index(max(lista))
        print(materia, "mejor:", alumnos[i], lista[i])
 
def reporte():
    res = []
    for i, nombre in enumerate(alumnos):
        suma = sum(lista[i] for lista in notas.values())
        res.append((nombre, round(suma / len(notas), 2)))
    res.sort(key=lambda x: x[1], reverse=True)
    for nombre, prom in res:
        print(nombre, prom)
 
promedio_materia()
mejor_alumno()
reporte()