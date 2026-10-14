"""
EJERCICIO 5: Búsqueda y filtrado de productos
Objetivo: crear buscar_productos(lista, termino), encontrar nombres que
contengan el término sin distinguir mayúsculas y ordenar por precio ascendente.
"""

productos = [
    {"nombre": "Laptop Lenovo", "categoria": "Computación", "precio": 2500.00},
    {"nombre": "Mouse inalámbrico", "categoria": "Accesorios", "precio": 75.50},
    {"nombre": "Laptop HP", "categoria": "Computación", "precio": 2200.00},
    {"nombre": "Teclado mecánico", "categoria": "Accesorios", "precio": 180.00},
    {"nombre": "Base para laptop", "categoria": "Accesorios", "precio": 95.00}
]

def buscar_productos(lista, termino):
    """Devuelve los productos cuyo nombre contiene el término buscado."""
    termino = termino.casefold()
    resultados = [
        producto for producto in lista
        if termino in producto["nombre"].casefold()
    ]
    return sorted(resultados, key=lambda producto: producto["precio"])

termino = input("Escribe qué producto deseas buscar: ").strip()
resultados = buscar_productos(productos, termino)

if resultados:
    print(f"\nResultados para '{termino}', ordenados por precio:")
    for producto in resultados:
        print(
            f"{producto['nombre']} | {producto['categoria']} | "
            f"S/ {producto['precio']:.2f}"
        )
else:
    print("No se encontraron productos con ese término.")
