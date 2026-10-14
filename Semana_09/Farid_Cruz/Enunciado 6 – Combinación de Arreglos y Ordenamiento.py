# Ejercicio 6 - Combinación de Arreglos y Ordenamiento

# Dos arreglos paralelos
productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Audífonos']
ventas    = [120, 340, 215, 98, 410]

# Combinarlos en una lista de diccionarios
lista = []
for producto, venta in zip(productos, ventas):
    lista.append({'producto': producto, 'ventas': venta})

# 1) Ordenar por ventas de mayor a menor
lista.sort(key=lambda d: d['ventas'], reverse=True)

# 2) Imprimir el ranking con posición (1°, 2°, etc.)
print("=== RANKING DE VENTAS ===")
for posicion, d in enumerate(lista, 1):
    print(f"{posicion}° {d['producto']}: {d['ventas']} ventas")

# 3) Promedio de ventas y cuáles están sobre la media
promedio = sum(ventas) / len(ventas)

print("-" * 30)
print(f"Promedio de ventas: {promedio:.1f}")
print("Productos sobre la media:")
for d in lista:
    if d['ventas'] > promedio:
        print(f"  {d['producto']} ({d['ventas']})")