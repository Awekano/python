#La fonction return permet de réutiliser des résultats obtenu 

def carre(nombre):
    print(f"Le carré de {nombre} est {nombre**2}")
    return nombre**2
resultat = carre(4)
print(resultat)