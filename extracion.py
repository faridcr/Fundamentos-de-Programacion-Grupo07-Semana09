# Dada una lista de strings con información mezclada como:
# ['Ana García - edad:25 - tel:987654321', 'Luis Pérez - edad:30 - tel:912345678']
# Usa expresiones regulares para extraer el nombre, la edad y el teléfono de cada registro
# y almacénalos en una lista de diccionarios.

import re

def extraer_informacion(registro):
        nombre = re.search(r'^([A-Za-z\s]+)', registro).group(1)
        edad = int(re.search(r'edad:(\d+)', registro).group(1))
        telefono = re.search(r'tel:(\d+)', registro).group(1)
        return {"nombre": nombre, "edad": edad, "telefono": telefono}

registros = [
        'Ana García - edad:25 - tel:987654321',
        'Luis Pérez - edad:30 - tel:912345678'
    ]

informacion_extraida = [extraer_informacion(registro) for registro in registros]

print(informacion_extraida)