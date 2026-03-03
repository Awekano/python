#Les méthodes add, remove et clear fonctionnent sur les ensembles car ils sont modifiables
villes = {"Paris", "Angoulême", "Marseille"}
print(villes)
villes.add("Angers")
print(villes)
villes.remove("Marseille")
print(villes)
#set() représente un ensemble vide
villes.clear()
print(villes)


#La méthode union() permet "d'additionner" les ensembles entre eux et de ne rien dupliquer car ce sont des ensembles
ensemble_1 = {"Asie", "Europe", "Océanie", "Afrique"}
ensemble_2 = {"Amérique du Nord", "Amérique du Sud", "Afrique"}
ensemble_3 = ensemble_1.union(ensemble_2)
print(ensemble_3)

#La méthode update() permet de mettre à jour un ensemble (BIEN METTRE LES {} SINON ÇA AJOUTE QUE LES CARACTÈRES UN À UN)
ensemble_3.update({"Antarctique"})
print(ensemble_3)