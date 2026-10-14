"""
EJERCICIO 3: Búsqueda simple en una lista de emails
Objetivo: contar emails de Gmail, filtrar los que terminan en .com
y comprobar si un correo está en la lista.
"""

emails = [
    "ana@gmail.com",
    "luis@outlook.com",
    "mia@gmail.com",
    "juan@yahoo.com"
]

# 1. Contar cuántos correos pertenecen a Gmail.
cantidad_gmail = 0
for email in emails:
    if email.lower().endswith("@gmail.com"):
        cantidad_gmail += 1

print("1. Cantidad de emails de Gmail:", cantidad_gmail)

# 2. Mostrar los correos que terminan en '.com'.
print("\n2. Emails que terminan en .com:")
for email in emails:
    if email.lower().endswith(".com"):
        print("-", email)

# 3. Comprobar si un correo está dentro de la lista usando 'in'.
correo_buscado = "luis@outlook.com"
if correo_buscado in emails:
    print(f"\n3. {correo_buscado} sí está en la lista.")
else:
    print(f"\n3. {correo_buscado} no está en la lista.")
