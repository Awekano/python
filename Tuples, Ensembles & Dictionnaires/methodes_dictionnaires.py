population = {"paris" : 2.148, "rome" : 2.873, "londres": 8.982}
print(population)
#La fonction keys() permet de retourner les clés d'un dictionnaire
print(population.keys())
#Et les mettre dans une liste
print(list(population.keys()))

#La fonction values() permet de retourner les valeurs d'un dictionnaire
print(population.values())
#Et les mettre dans une liste
print(list(population.values()))

#La fonction items() permet de retourner une liste de tuples avec les clés et les valeurs d'un dictionnaire
print(population.items())
print(list(population.items()))