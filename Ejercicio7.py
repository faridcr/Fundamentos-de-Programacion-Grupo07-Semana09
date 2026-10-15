
import re

registros = [
    "Ana García - edad:25 - tel:987654321",
    "Luis Pérez - edad:30 - tel:912345678"
]

personas = []

for registro in registros:
    datos = re.search(r"(.+?) - edad:(\d+) - tel:(\d+)", registro)

    if datos:
        persona = {
            "nombre": datos.group(1),
            "edad": int(datos.group(2)),
            "telefono": datos.group(3)
        }

        personas.append(persona)

for persona in personas:
    print("Nombre:", persona["nombre"])
    print("Edad:", persona["edad"])
    print("Telefono:", persona["telefono"])
    print()
