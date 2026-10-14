"""
EJERCICIO 6: Combinación de arreglos y ordenamiento
Objetivo: combinar productos y ventas en diccionarios, ordenar de mayor
a menor, mostrar el ranking y calcular el promedio de ventas.
"""

productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora"]
ventas = [35, 80, 60, 25, 40]

# Las posiciones de ambas listas corresponden al mismo producto.
catalogo = []
for i in range(len(productos)):
    catalogo.append({"producto": productos[i], "ventas": ventas[i]})

# Orden descendente por ventas.
catalogo_ordenado = sorted(
    catalogo, key=lambda elemento: elemento["ventas"], reverse=True
)

print("RANKING DE VENTAS")
for posicion, elemento in enumerate(catalogo_ordenado, start=1):
    print(f"{posicion}. {elemento['producto']} - {elemento['ventas']} ventas")

promedio = sum(ventas) / len(ventas)
print(f"\nPromedio de ventas: {promedio:.2f}")
print("Productos por encima de la media:")
for elemento in catalogo_ordenado:
    if elemento["ventas"] > promedio:
        print(f"- {elemento['producto']}: {elemento['ventas']} ventas")
