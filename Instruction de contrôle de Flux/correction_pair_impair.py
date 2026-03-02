#Exerice il faut coder un programme qui en fonction de l'entrée utilisateur dira si le chiffre est pair ou impair CORRECTION
nombre = int(input("Entre un nombre entier : "))

if nombre % 2 == 0:
    print(f"Le nombre {nombre} est pair")
else:
    print(f"Le nombre {nombre} est impair")