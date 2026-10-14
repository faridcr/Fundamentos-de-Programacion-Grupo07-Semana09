# ---------- Ejercicio 9: buscador con regex ----------

from Lib import re

catalogo = [
    {'titulo': 'Python a fondo',        'autor': 'Óscar Ramírez', 'año': 2021},
    {'titulo': 'Aprende Python rápido', 'autor': 'Ana Python',    'año': 2019},
    {'titulo': 'Estructuras de datos',  'autor': 'Python Guru',   'año': 2018},
    {'titulo': 'Bases de datos',        'autor': 'Luis Soto',     'año': 2020},
]
 
def buscador(catalogo, query):
    res = []
    for libro in catalogo:
        puntos = 0
        if re.search(query, libro['titulo'], re.I):
            puntos += 2
        if re.search(query, libro['autor'], re.I):
            puntos += 1
        if puntos > 0:
            res.append((puntos, libro))
    res.sort(key=lambda x: (-x[0], x[1]['año']))
    return res
 
for puntos, libro in buscador(catalogo, "python"):
    print(puntos, "pts -", libro['titulo'], "-", libro['autor'], libro['año'])