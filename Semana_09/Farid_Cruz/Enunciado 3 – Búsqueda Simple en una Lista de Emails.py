# Ejercicio 3 - Búsqueda Simple en una Lista de Emails

emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

# 1) Cuántos emails son de Gmail
cantidad_gmail = 0
for email in emails:
    if email.endswith('@gmail.com'):
        cantidad_gmail += 1
print(f"1) Emails de Gmail: {cantidad_gmail}")

# 2) Solo los emails que terminan en '.com'
print("2) Emails que terminan en '.com':")
for email in emails:
    if email.endswith('.com'):
        print("  ", email)

# 3) Verificar si 'luis@outlook.com' está en la lista (operador 'in')
buscado = 'luis@outlook.com'
if buscado in emails:
    print(f"3) '{buscado}' SÍ está en la lista")
else:
    print(f"3) '{buscado}' NO está en la lista")