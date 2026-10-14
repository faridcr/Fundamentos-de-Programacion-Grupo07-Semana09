"""
EJERCICIO 7: Extracción con expresiones regulares
Objetivo: extraer nombre, edad y teléfono de cada texto y guardar los datos
en una lista de diccionarios.
"""

import re

registros = [
    "Ana García - edad:25 - tel:987654321",
    "Luis Pérez - edad:30 - tel:912345678"
]

personas = []
patron = re.compile(
    r"(?P<nombre>.+?) - edad:(?P<edad>\d+) - tel:(?P<telefono>\d+)"
)

for registro in registros:
    coincidencia = patron.search(registro)
    if coincidencia:
        personas.append({
            "nombre": coincidencia.group("nombre"),
            "edad": int(coincidencia.group("edad")),
            # El teléfono se guarda como texto para conservar posibles ceros iniciales.
            "telefono": coincidencia.group("telefono")
        })

print("DATOS EXTRAÍDOS")
for persona in personas:
    print(persona)
