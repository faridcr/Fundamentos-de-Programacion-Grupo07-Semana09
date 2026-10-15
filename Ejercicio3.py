
emails = ["ana@gmail.com", "luis@outlook.com",
          "mia@gmail.com", "juan@yahoo.com"]

contador = 0

for email in emails:
    if email.endswith("@gmail.com"):
        contador += 1

print("Cantidad de Gmail:", contador)

print("\nEmails que terminan en .com:")
for email in emails:
    if email.endswith(".com"):
        print(email)

if "luis@outlook.com" in emails:
    print("\nLuis esta en la lista")
else:
    print("\nLuis no esta en la lista")
