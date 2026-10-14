"""
EJERCICIO 2: Ordenamiento alfanumérico de nombres
Objetivo:
1. Mostrar la lista original.
2. Ordenar alfabéticamente sin distinguir mayúsculas/minúsculas.
3. Crear una nueva lista ordenada en forma descendente.
"""

# Lista original de nombres
nombres = ["Carlos", "ana", "Beatriz", "david", "Elena"]

# 1. Mostrar la lista original
print("1. Lista original:")
print(nombres)

# 2. Ordenar la lista original alfabéticamente (A a Z)
# key=str.lower permite comparar los nombres en minúsculas.
nombres.sort(key=str.lower)

print("\\n2. Lista ordenada alfabéticamente (A a Z):")
print(nombres)

# 3. Crear una lista nueva en orden descendente (Z a A)
# sorted() crea una nueva lista y reverse=True invierte el orden.
nombres_descendentes = sorted(nombres, key=str.lower, reverse=True)

print("\\n3. Lista ordenada en forma descendente (Z a A):")
print(nombres_descendentes)
