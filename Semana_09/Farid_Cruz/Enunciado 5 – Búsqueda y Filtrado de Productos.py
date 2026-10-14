# Ejercicio 5 - Búsqueda y Filtrado de Productos

productos = [
    {'nombre': 'Laptop Lenovo',    'categoria': 'Cómputo',    'precio': 2500},
    {'nombre': 'Mouse Logitech',   'categoria': 'Accesorios', 'precio': 45},
    {'nombre': 'Teclado Mecánico', 'categoria': 'Accesorios', 'precio': 120},
    {'nombre': 'Monitor LG',       'categoria': 'Cómputo',    'precio': 800},
    {'nombre': 'Laptop HP',        'categoria': 'Cómputo',    'precio': 2100},
    {'nombre': 'Mouse Gamer',      'categoria': 'Gamer',      'precio': 90},
]


def buscar_productos(lista, termino):
    resultados = []
    for p in lista:
        if termino.lower() in p['nombre'].lower():
            resultados.append(p)

    resultados.sort(key=lambda p: p['precio'])
    return resultados


for termino in ['LAPTOP', 'mouse', 'tablet']:
    print(f"Búsqueda: {termino}")
    encontrados = buscar_productos(productos, termino)
    if not encontrados:
        print("  No se encontraron productos.")
    for p in encontrados:
        print(f"  {p['nombre']} - S/ {p['precio']}")