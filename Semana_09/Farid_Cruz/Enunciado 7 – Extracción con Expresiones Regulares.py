# Ejercicio 7 - Extracción con Expresiones Regulares
import re

registros = [
    'Ana García - edad:25 - tel:987654321',
    'Luis Pérez - edad:30 - tel:912345678',
    'Mía Torres - edad:22 - tel:955443322',
]

# Patrón con 3 grupos entre paréntesis: nombre, edad, teléfono
patron = r'(.+?) - edad:(\d+) - tel:(\d+)'

personas = []
for texto in registros:
    match = re.search(patron, texto)
    if match:
        personas.append({
            'nombre': match.group(1),
            'edad': int(match.group(2)),
            'telefono': match.group(3),
        })

# Mostrar la lista de diccionarios
for p in personas:
    print(p)

print("-" * 30)
for p in personas:
    print(f"{p['nombre']} tiene {p['edad']} años y su teléfono es {p['telefono']}")