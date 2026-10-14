
# Tienes la lista: emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']
# 1) Imprime cuántos emails son de Gmail.
# 2) Muestra solo los emails que terminan en '.com'.
# 3) Verifica si 'luis@outlook.com' está en la lista (usa 'in').

emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']


gmail_count = sum(1 for email in emails if email.endswith('@gmail.com'))
print(f"numeros de email de Gmail: {gmail_count}")

com_emails = [email for email in emails if email.endswith('.com')]
print("Emails que terminan en '.com':", com_emails)


if 'luis@outlook.com' in emails:
    print("luis@outlook.com está en la lista.")
else:
    print("luis@outlook.com no está en la lista.")