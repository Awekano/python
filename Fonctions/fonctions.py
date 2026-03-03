#Une fonction doit être déclaré içi la fonction hello_world() renvoie "Hello, world !" via la fonction primaire de python print()
def hello_world():
    print("Hello, world !")

hello_world()

def jeu():
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

jeu()

#On peut résumer des codes entiers en une seule commande
#Içi le code de "Devine le nombre" est appelé par la fonction créer précedemment : jeu()