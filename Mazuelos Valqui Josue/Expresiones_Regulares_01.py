# ---------- Ejercicio 1: arreglos paralelos ----------

print("--- Ejercicio 1 ---")
nombres = ["Laptop", "Mouse", "Teclado", "Monitor"]
precios = [2500, 35, 90, 750]
stock = [15, 100, 60, 25]
 
total = 0
for n, p, s in zip(nombres, precios, stock):
    print(n, "- precio:", p, "- cantidad:", s)
    total += p * s
print("Total del inventario:", total)