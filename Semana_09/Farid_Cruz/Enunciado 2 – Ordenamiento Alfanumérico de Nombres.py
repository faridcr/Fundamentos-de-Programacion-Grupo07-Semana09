# Ejercicio 2 - Ordenamiento Alfanumérico de Nombres

nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']

# 1) Imprimir la lista sin modificar
print("1) Lista original:")
print(nombres)

# 2) Ordenar alfabéticamente ignorando mayúsculas con sort() (modifica la lista original)
nombres.sort(key=str.lower)
print("\n2) Ordenada con sort(key=str.lower):")
print(nombres)

# 3) Nueva lista en orden descendente con sorted() (no modifica la original)
descendente = sorted(nombres, key=str.lower, reverse=True)
print("\n3) Nueva lista descendente con sorted():")
print(descendente)

# 4) Resultados de cada paso (la original quedó ordenada por el sort() del paso 2)
print("\n4) Resumen de resultados:")
print(f"Lista original (ya ordenada por sort): {nombres}")
print(f"Lista descendente (sorted):          {descendente}")