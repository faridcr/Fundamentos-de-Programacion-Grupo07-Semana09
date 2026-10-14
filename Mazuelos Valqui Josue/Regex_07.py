import re

print("\n--- Ejercicio 7 ---")
registros = ['Ana García - edad:25 - tel:987654321',
             'Luis Pérez - edad:30 - tel:912345678']

personas = []
for r in registros:
    nombre, edad, tel = re.findall(r'(.+?) - edad:(\d+) - tel:(\d+)', r)[0]
    personas.append({'nombre': nombre, 'edad': int(edad), 'telefono': tel})

print(personas)