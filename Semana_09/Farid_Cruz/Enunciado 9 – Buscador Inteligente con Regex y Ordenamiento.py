# Ejercicio 9 - Buscador Inteligente con Regex y Ordenamiento
import re

catalogo = [
    {'titulo': 'Cien años de soledad',              'autor': 'Gabriel García Márquez', 'año': 1967},
    {'titulo': 'El amor en los tiempos del cólera', 'autor': 'Gabriel García Márquez', 'año': 1985},
    {'titulo': 'Gabriel y el Mar',                  'autor': 'Ana Torres',             'año': 2010},
    {'titulo': 'Python a fondo',                    'autor': 'Óscar Ramírez Jiménez',  'año': 2021},
    {'titulo': 'Principios de programación',        'autor': 'Carlos Chacón Sartori',  'año': 2023},
    {'titulo': 'La ciudad y los perros',            'autor': 'Mario Vargas Llosa',     'año': 1963},
    {'titulo': 'Conversación en La Catedral',       'autor': 'Mario Vargas Llosa',     'año': 1969},
]


def buscador(catalogo, query):
    """Busca 'query' (regex, sin importar mayúsculas) en título y autor.
    Título vale 2 puntos y autor 1 punto. Devuelve los resultados ordenados
    por puntaje (mayor a menor) y luego por año (menor a mayor)."""
    resultados = []
    for libro in catalogo:
        puntaje = 0
        if re.search(query, libro['titulo'], re.IGNORECASE):
            puntaje += 2
        if re.search(query, libro['autor'], re.IGNORECASE):
            puntaje += 1

        if puntaje > 0:
            resultados.append({
                'titulo': libro['titulo'],
                'autor': libro['autor'],
                'año': libro['año'],
                'puntaje': puntaje,
            })

    # Puntaje descendente (el signo - invierte el orden) y año ascendente
    resultados.sort(key=lambda r: (-r['puntaje'], r['año']))
    return resultados


for query in ['gabriel', 'MARIO', 'python', 'xyz']:
    print(f"\nBúsqueda: '{query}'")
    encontrados = buscador(catalogo, query)
    if not encontrados:
        print("  Sin resultados.")
    for r in encontrados:
        print(f"  [{r['puntaje']} pts] {r['titulo']} - {r['autor']} ({r['año']})")