
productos = ["Arroz", "Azucar", "Leche", "Aceite"]
precios = [5.0, 4.0, 4.5, 10.0]
cantidades = [10, 8, 12, 5]

total = 0

for i in range(len(productos)):
    print(productos[i], "- Precio: S/", precios[i], "- Cantidad:", cantidades[i])

    subtotal = precios[i] * cantidades[i]
    total = total + subtotal

print("Precio total del inventario: S/", total)
