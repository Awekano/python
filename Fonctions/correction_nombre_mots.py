#Définir une fonction qui prendra en arguments une variables qui est une chaîne de caractère CORRECTION
#Cette fonction retournera une variable qui comptera le nombre de mots dans cette chaîne de caractère CORRECTION
def nombre_mots(texte):
    return texte.split(" ")

n = nombre_mots(input("Entrez une phrase : "))
print(f"Votre phrase contient {len(n)} mots")