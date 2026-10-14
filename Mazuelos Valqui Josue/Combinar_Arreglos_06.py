# ---------- Ejercicio 6: combinar arreglos ----------

prod = ['Laptop', 'Mouse', 'Teclado', 'Monitor']
ventas = [120, 340, 210, 95]
 
datos = [{'producto': p, 'ventas': v} for p, v in zip(prod, ventas)]
datos.sort(key=lambda d: d['ventas'], reverse=True)
 
for i, d in enumerate(datos, 1):
    print(f"{i}° {d['producto']}: {d['ventas']}")
 
promedio = sum(ventas) / len(ventas)
print("Promedio:", promedio)
for d in datos:
    if d['ventas'] > promedio:
        print("Sobre la media:", d['producto'])
        