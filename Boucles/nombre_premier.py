#Créer un code qui permet de déterminer si un nombre est premier

nombre = int(input("Nombre : "))
divisible = False

for i in range(2, nombre):
    if (nombre % i) == 0:
        divisible = True
        break
if divisible:
    print(f"Le nombre {nombre} n'est pas un nombre premier")
else:
    print(f"Le nombre {nombre} est un nombre premier")