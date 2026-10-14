# ---------- Ejercicio 3: emails ----------

emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']
 
print("Emails de Gmail:", sum(1 for e in emails if 'gmail' in e))
print("Terminan en .com:", [e for e in emails if e.endswith('.com')])
print("¿Está luis@outlook.com?", 'luis@outlook.com' in emails)
 