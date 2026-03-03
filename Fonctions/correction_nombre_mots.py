#Définir une fonction qui prendra en arguments une variables qui est une chaîne de caractère
#Cette fonction retournera une variable qui comptera le nombre de mots dans cette chaîne de caractère
def nombre_mots(texte):
    return texte.split(" ")

n = nombre_mots(input("Entrez une phrase : "))
print(f"Votre phrase contient {len(n)} mots")