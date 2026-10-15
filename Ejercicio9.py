
import re

catalogo = [
    {"titulo": "Python Basico", "autor": "Carlos Perez", "año": 2020},
    {"titulo": "Aprende Python", "autor": "Ana Torres", "año": 2023},
    {"titulo": "Programacion Java", "autor": "Python Martinez", "año": 2021},
    {"titulo": "Python Avanzado", "autor": "Luis Gomez", "año": 2022}
]

def buscador(catalogo, query):
    resultados = []

    for libro in catalogo:
        puntos = 0

        if re.search(query, libro["titulo"], re.IGNORECASE):
            puntos += 2

        if re.search(query, libro["autor"], re.IGNORECASE):
            puntos += 1

        if puntos > 0:
            resultado = libro.copy()
            resultado["puntos"] = puntos
            resultados.append(resultado)

    resultados.sort(key=lambda libro: (-libro["puntos"], libro["año"]))

    return resultados


query = input("Ingrese palabra a buscar: ")

try:
    encontrados = buscador(catalogo, query)

    if len(encontrados) == 0:
        print("No se encontraron resultados")
    else:
        for libro in encontrados:
            print(libro["titulo"], "-", libro["autor"],
                  "- Año:", libro["año"],
                  "- Puntos:", libro["puntos"])

except re.error:
    print("ERROR: Expresion regular incorrecta")
