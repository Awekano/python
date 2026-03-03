#Les arguments arbitraire sont utiles lorsque le nombre d'arguments est inconnu ou différents selon les personnes qui utilisent la fonction
def loto(**numeros):
    print(numeros)
loto(n1=2,n2=10,n3=16,n4=30,n5=36, chance = 6)