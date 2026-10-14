
# Ejercicio 1: Registro de productos

# Creamos tres listas paralelas
nombres = ["Laptop", "Mouse", "Teclado", "Monitor"]
precios = [2500.00, 45.00, 120.00, 850.00]
cantidades = [3, 10, 5, 4]

# Variable para acumular el valor total del inventario
total_inventario = 0

print("=== REPORTE DE PRODUCTOS ===")

# Recorremos los productos utilizando sus posiciones
for i in range(len(nombres)):
    print(
        f"Producto: {nombres[i]} | "
        f"Precio: S/ {precios[i]:.2f} | "
        f"Stock: {cantidades[i]}"
    )

    # Calculamos el valor de cada producto en stock
    subtotal = precios[i] * cantidades[i]

    # Sumamos el subtotal al total del inventario
    total_inventario += subtotal

print("--------------------------------")
print(f"Valor total del inventario: S/ {total_inventario:.2f}")
