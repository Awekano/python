#Les arguments sont des données nécessaires pour une fonctions içi dans la fonction message() on veut un prénom, le code va retourner l'entrée
#utilisateur dans la fonction dans la fonction print()
def message(prenom):
    print(f"Bonjour {prenom}")



def aire_cercle(rayon):
    print("L'aire du cercle est :", 3.14*rayon**2)

message(input("Quel est ton prenom : "))
aire_cercle(float(input("Entrez le rayon du cercle : ")))

#Il est possible de mettre plusieurs arguments dans une seule fonction
def presentation(prenom, age):
    print(f"Bonjour {prenom} tu as {age} ans")

presentation(input("Quel est ton prénom : "), int(input("Quel est ton âge : ")))
