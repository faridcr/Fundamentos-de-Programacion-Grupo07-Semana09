# Ejercicio 1 - Registro de Productos con Arreglos Paralelos

# Tres arreglos paralelos (el índice i corresponde al mismo producto)
nombres   = ['Laptop', 'Mouse', 'Teclado', 'Monitor']
precios   = [2500.0, 45.5, 120.0, 800.0]
cantidades = [15, 100, 60, 25]

# Reporte: una línea por producto
print("=== REPORTE DE INVENTARIO ===")
for nombre, precio, cantidad in zip(nombres, precios, cantidades):
    print(f"{nombre}: precio S/ {precio:.2f} | stock: {cantidad}")

# Precio total del inventario (precio x cantidad de todos)
total = 0
for i in range(len(nombres)):
    total += precios[i] * cantidades[i]

print("-" * 30)
print(f"Valor total del inventario: S/ {total:.2f}")