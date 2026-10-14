# Tienes dos arreglos paralelos: productos (strings) y ventas (enteros).
# Combínalos en una lista de diccionarios, luego:
# 1) Ordena por ventas de mayor a menor.
# 2) Imprime el ranking con posición (1°, 2°, etc.).
# 3) Calcula el promedio de ventas e indica cuáles están sobre la media

productos = ["Arroz", "Azúcar", "Aceite", "Leche", "Pan", "Mantequilla"]
ventas = [100, 150, 80, 120, 200, 90]

productos_ventas = [{"nombre": p, "ventas": v} for p, v in zip(productos, ventas)]

productos_ventas_ordenados = sorted(productos_ventas, key=lambda x: x['ventas'], reverse=True)

print("Ranking de productos por ventas:")
for i, producto in enumerate(productos_ventas_ordenados, start=1):
    print(f"{i}° {producto['nombre']}: {producto['ventas']} unidades")

promedio_ventas = sum(p['ventas'] for p in productos_ventas) / len(productos_ventas)
print(f"\nPromedio de ventas: {promedio_ventas:.2f}")

print("\nProductos sobre la media:")
for producto in productos_ventas:
    if producto['ventas'] > promedio_ventas:
        print(f"{producto['nombre']}: {producto['ventas']} unidades")