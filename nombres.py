
# Dada la lista de nombres: ['Carlos','ana','Beatriz','david','Elena']
# 1) Imprímela sin modificar.
# 2) Ordénala alfabéticamente ignorando mayúsculas con sort().
# 3) Crea una nueva lista ordenada en orden descendente usando sorted().
# 4) Muestra los resultados de cada paso.
nombres = ['Carlos','ana','Beatriz','david','Elena']
print("Lista original:", nombres)

nombres.sort(key=str.lower)
print("Lista ordenada (ascendente):", nombres)

nombres_descendente = sorted(nombres, key=str.lower, reverse=True)
print("Lista ordenada (descendente):", nombres_descendente)