# ---------- Ejercicio 2: ordenar nombres ----------

lista = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']
print("Original:", lista)
 
copia = lista.copy()
copia.sort(key=str.lower)
print("sort() sin mayúsculas:", copia)
 
desc = sorted(lista, key=str.lower, reverse=True)
print("sorted() descendente:", desc)