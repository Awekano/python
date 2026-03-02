#Faire un programme qui permet de calculer l'IMC d'une personne, formule : poids/taille² CORRECTION
poids = float(input("Quel est votre poids (en Kg) : "))
taille = float(input("Quel est votre taille (en m): "))
IMC = poids/(taille**2)
print(f"L'IMC d'une personne de {poids} kg et de {taille} m est de {IMC}kg/m²")
