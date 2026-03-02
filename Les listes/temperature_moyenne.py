#Objectif : calculer la moyenne des température de la liste temperatures
temperatures = [23,22,19,26,24,28,26]
moyenne = 0
for i in temperatures:
    moyenne = moyenne + i

moyenne = moyenne / len(temperatures)

print(f"La moyenne des températures est de {moyenne}C°")