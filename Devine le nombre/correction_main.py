#Faire un jeu devine le nombre entre 1 et 100
#Indication + ou - pour aider le joueur 
import random
nombre_aleatoire = random.randint(1,100)
nombre_utilisateur = int(input("Choix du nombre : "))

while nombre_aleatoire != nombre_utilisateur:
    if nombre_utilisateur < nombre_aleatoire:
        print("C'est plus haut !")
        nombre_utilisateur = int(input("Recommence : "))
    elif nombre_utilisateur > nombre_aleatoire:
        print("C'est plus bas ! ")
        nombre_utilisateur = int(input("Recommence : "))
    else:
        break
print(f"Bravo tu as trouvé le nombre aléatoire qui étais {nombre_aleatoire}")
