
productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
ventas = [20, 50, 30, 40]

lista = []

for i in range(len(productos)):
    lista.append({
        "producto": productos[i],
        "ventas": ventas[i]
    })

lista.sort(key=lambda dato: dato["ventas"], reverse=True)

print("RANKING DE VENTAS")

for i in range(len(lista)):
    print(i + 1, "-", lista[i]["producto"],
          "- Ventas:", lista[i]["ventas"])

total = 0

for venta in ventas:
    total += venta

promedio = total / len(ventas)

print("\nPromedio de ventas:", promedio)

print("\nProductos sobre el promedio:")

for producto in lista:
    if producto["ventas"] > promedio:
        print(producto["producto"])
