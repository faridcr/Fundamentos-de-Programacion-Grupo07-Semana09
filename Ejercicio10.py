
import re

texto = """
Python es un lenguaje de programación.
Python permite aprender programación.
La programación es importante y Python es útil.
"""

palabras = re.findall(r"[^\W\d_]+(?:['’][^\W\d_]+)*", texto.lower())

frecuencias = {}

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

ordenadas = sorted(
    frecuencias.items(),
    key=lambda dato: (-dato[1], dato[0])
)

print("TOP 5 PALABRAS")

for i in range(min(5, len(ordenadas))):
    print(i + 1, "-", ordenadas[i][0], ":", ordenadas[i][1])

print("\nPALABRAS UNICAS")

unicas = sorted(frecuencias.keys())

for palabra in unicas:
    print(palabra)
