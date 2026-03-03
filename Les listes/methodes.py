#Découverte des méthodes de liste clear, count, index, sort, min, max, sum
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

#index() permet de connaitre la position d'un élément dans une liste
idx = loto.index(69)
print(idx)

#permet d'ordonner la liste par ordre alphabétique ou par ordre de grandeur
loto.sort()
print(loto)

achats = [15,3.2,20,15,5,2.5]
print(achats)
#La fonction min permet de retourner la plus petite somme de la liste
print(min(achats))
#La fonction max permet de retourner la plus grande somme de la liste
print(max(achats))
#La fonction sum permet de retourner la somme de la liste
print(sum(achats))