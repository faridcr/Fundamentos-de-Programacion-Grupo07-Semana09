
# Crea tres arreglos paralelos para almacenar información de 4 productos: nombres, precios y cantidades en stock.
# Imprime un reporte que muestre cada producto con su precio y cantidad en una sola línea por producto.
# Además, calcula e imprime el precio total del inventario (precio × cantidad para todos).



nombres = ["Arroz", "Azúcar", "Aceite", "Leche"]
precios = [3.50, 2.80, 8.00, 4.20]  
cantidades = [50, 30, 20, 40]

print("\n--- INVENTARIO DE ABARROTES ---")
for i in range(len(nombres)):
    print(f"{nombres[i]} - Precio: S/{precios[i]} - Stock: {cantidades[i]}")

# Calcular precio total del inventario
total = 0
for i in range(len(nombres)):
    total += precios[i] * cantidades[i]

print("\n Valor total del inventario: S/", round(total, 2))
