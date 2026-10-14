
# Tienes una lista de diccionarios de productos con 'nombre', 'categoria' y 'precio'.
# Implementa una función buscar_productos(lista, termino) que devuelva todos los productos
# cuyo nombre contenga el término de búsqueda (sin importar mayúsculas).
# Además, ordena los resultados por precio de menor a mayor.
def buscar_productos(lista, termino):
    resultados = [producto for producto in lista if termino.lower() in producto['nombre'].lower()]
    return resultados
productos = [
    {"nombre": "Arroz", "categoria": "Abarrotes", "precio": 3.50},
    {"nombre": "Azúcar", "categoria": "Abarrotes", "precio": 2.80},
    {"nombre": "Aceite", "categoria": "Abarrotes", "precio": 8.00},
    {"nombre": "Leche", "categoria": "Lácteos", "precio": 4.20},
    {"nombre": "Pan", "categoria": "Panadería", "precio": 1.50},
    {"nombre": "Mantequilla", "categoria": "Lácteos", "precio": 5.00}
]
termino_busqueda = "a"
resultados = buscar_productos(productos, termino_busqueda)
# Ordenar resultados por precio de menor a mayor    
resultados_ordenados = sorted(resultados, key=lambda x: x['precio'])
print(f"Productos que contienen '{termino_busqueda}':") 
for producto in resultados_ordenados:
    print(f"{producto['nombre']} - Categoría: {producto['categoria']} - Precio: S/{producto['precio']}")