
productos = [
    {"nombre": "Laptop HP", "categoria": "Computadoras", "precio": 2500},
    {"nombre": "Mouse Logitech", "categoria": "Accesorios", "precio": 80},
    {"nombre": "Laptop Lenovo", "categoria": "Computadoras", "precio": 2200},
    {"nombre": "Teclado", "categoria": "Accesorios", "precio": 120}
]

def buscar_productos(lista, termino):
    resultados = []

    for producto in lista:
        if termino.lower() in producto["nombre"].lower():
            resultados.append(producto)

    resultados.sort(key=lambda producto: producto["precio"])
    return resultados


termino = input("Ingrese producto a buscar: ")
encontrados = buscar_productos(productos, termino)

if len(encontrados) == 0:
    print("No se encontraron productos")
else:
    for producto in encontrados:
        print(producto["nombre"], "- S/", producto["precio"])
