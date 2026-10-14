
nombres = ["Carlos", "ana", "Beatriz", "david", "Elena"]

print("Lista original:")
print(nombres)

nombres.sort(key=str.lower)

print("Lista ordenada alfabeticamente:")
print(nombres)

descendente = sorted(nombres, key=str.lower, reverse=True)

print("Lista ordenada de forma descendente:")
print(descendente)
