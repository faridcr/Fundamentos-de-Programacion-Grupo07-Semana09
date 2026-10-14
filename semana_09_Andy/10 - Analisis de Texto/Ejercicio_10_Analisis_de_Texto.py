"""
EJERCICIO 10: Análisis de texto y estadísticas de palabras
Objetivo: extraer palabras con regex, contar frecuencias sin distinguir
mayúsculas, ordenar por frecuencia descendente y alfabéticamente en empates,
mostrar las cinco más frecuentes y las palabras únicas ordenadas.
"""

import re
from collections import Counter

texto = """
Python es un lenguaje sencillo. Python permite aprender programación.
Aprender Python ayuda a resolver problemas, y resolver problemas requiere práctica.
La práctica hace que aprender sea más sencillo.
"""

# \w puede incluir números y guiones bajos; este patrón captura letras
# Unicode y permite apóstrofes dentro de palabras.
patron = r"[^\W\d_]+(?:['’][^\W\d_]+)*"
palabras = re.findall(patron, texto.casefold())

frecuencias = Counter(palabras)

# Orden: más frecuente primero; si empatan, orden alfabético.
ranking = sorted(frecuencias.items(), key=lambda item: (-item[1], item[0]))

print("TOP 5 PALABRAS MÁS FRECUENTES")
for palabra, cantidad in ranking[:5]:
    print(f"{palabra}: {cantidad}")

palabras_unicas = sorted(
    palabra for palabra, cantidad in frecuencias.items() if cantidad == 1
)

print("\nPALABRAS QUE APARECEN UNA SOLA VEZ (ordenadas)")
print(", ".join(palabras_unicas) if palabras_unicas else "No hay palabras únicas.")
