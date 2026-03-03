#Le docstring permet de documenter une fonction afin d'expliquer comment l'utiliser et à quoi elle sert (ultra-utile)
def calcul_aire(rayon):
    """Cette fonction permet de calculer une aire à partir d'un rayon"""
    return 3.14*rayon**2

print(calcul_aire.__doc__)
print(calcul_aire(10))