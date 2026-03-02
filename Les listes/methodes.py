#Découverte des méthodes de liste clear, count, index, sort
villes = ["Angers", "Paris", "Angoulême"]
print(villes)
#clear() permet de vider une liste
villes.clear()
print(villes)

loto = [2,3,8,69,2,78,67,12,2]
print(loto)
#count() permet de compter le nombre d'occurence dans une liste
occurence = loto.count(2)
print(occurence)

#index() permet de connaitre la position d'un élement dans une liste
idx = loto.index(69)
print(idx)

#permet d'ordonner la liste par ordre alphabétique ou par ordre de grandeur
loto.sort()
print(loto)
