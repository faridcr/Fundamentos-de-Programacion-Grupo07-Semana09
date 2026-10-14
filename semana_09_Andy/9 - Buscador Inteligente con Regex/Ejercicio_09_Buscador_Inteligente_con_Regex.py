"""
EJERCICIO 9: Buscador inteligente con regex y ordenamiento
Objetivo: buscar una consulta en título y autor ignorando mayúsculas,
asignar 2 puntos por coincidencia en título y 1 por autor, y ordenar
por puntaje descendente y luego por año descendente (más reciente primero).
"""

import re

catalogo = [
    {"titulo": "Python desde cero", "autor": "Ana Torres", "año": 2022},
    {"titulo": "Introducción a la programación", "autor": "Luis Pérez", "año": 2019},
    {"titulo": "Python avanzado", "autor": "Carlos Ruiz", "año": 2024},
    {"titulo": "Bases de datos", "autor": "Ana Python García", "año": 2021},
    {"titulo": "Algoritmos", "autor": "María López", "año": 2023}
]

def buscador(catalogo, query):
    """Busca query como expresión regular y devuelve resultados con puntaje."""
    patron = re.compile(query, re.IGNORECASE)
    resultados = []

    for libro in catalogo:
        coincide_titulo = bool(patron.search(libro["titulo"]))
        coincide_autor = bool(patron.search(libro["autor"]))

        puntaje = (2 if coincide_titulo else 0) + (1 if coincide_autor else 0)
        if puntaje > 0:
            resultado = libro.copy()
            resultado["puntaje"] = puntaje
            resultados.append(resultado)

    # Primero mayor puntaje; en empate, año más reciente.
    return sorted(
        resultados,
        key=lambda libro: (-libro["puntaje"], -libro["año"])
    )

consulta = input("Escribe una búsqueda (texto o patrón regex): ").strip()
try:
    resultados = buscador(catalogo, consulta)
    if resultados:
        print("\nRESULTADOS")
        for libro in resultados:
            print(
                f"Puntaje: {libro['puntaje']} | Año: {libro['año']} | "
                f"{libro['titulo']} — {libro['autor']}"
            )
    else:
        print("No se encontraron coincidencias.")
except re.error as error:
    print("La expresión regular no es válida:", error)
