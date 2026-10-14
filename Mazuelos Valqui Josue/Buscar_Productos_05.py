# ---------- Ejercicio 5: buscar productos ----------

productos = [
    {'nombre': 'Laptop HP',     'categoria': 'Computo',    'precio': 2500},
    {'nombre': 'Mouse',         'categoria': 'Accesorios', 'precio': 45},
    {'nombre': 'Laptop Gamer',  'categoria': 'Computo',    'precio': 4200},
    {'nombre': 'Laptop Lenovo', 'categoria': 'Computo',    'precio': 2800},
]
 
def buscar_productos(lista, termino):
    res = [p for p in lista if termino.lower() in p['nombre'].lower()]
    return sorted(res, key=lambda p: p['precio'])
 
for p in buscar_productos(productos, "LAPTOP"):
    print(p['nombre'], p['precio'])