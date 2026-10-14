import re

texto = "Python es fácil. La sintaxis de Python es clara y el lenguaje es potente. Aprende Python, es genial y la comunidad es amable."

# 1) Extraer palabras (solo letras y apóstrofes)
palabras = re.findall(r"[a-záéíóúüñ']+", texto.lower())

# 2) Contar la frecuencia de cada palabra
frecuencia = {}
for p in palabras:
    frecuencia[p] = frecuencia.get(p, 0) + 1

# 3) Ordenar por frecuencia (mayor a menor) y luego alfabéticamente
orden = sorted(frecuencia.items(), key=lambda x: (-x[1], x[0]))

# 4) Mostrar resultados
print("Top 5:", orden[:5])
print("Únicas:", sorted(frecuencia))