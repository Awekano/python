#Comment fonctionne la boucle for() avec un dictionnaire
population = {"angers" : 157555, "angoulême": 41908, "narbonne" : 56692 }
print(population)

#Première méthode pas très propre
for p in population:
    print(p, population[p])

#Deuxième méthode plus propre
for ville, habitants in population.items():
    print(ville,habitants)