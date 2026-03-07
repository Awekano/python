#Une même méthode qui retourne 2 résultats différents
class Forme:
    def __init__(self, nom):
        self.nom = nom
    def aire(self):
        print("Calcul d'aire")
    def info(self):
        print(f"Classe {self.nom}")

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        super().__init__("Rectangle")
        self.longueur = longueur
        self.largeur = largeur
    def aire(self):
        print("Aire : ",self.largeur*self.longueur)

class Cercle(Forme):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon
    def aire(self):
        print("Aire : ",3.14*self.rayon**2)

rect = Rectangle(5,4)
rect.info()
rect.aire()
cer = Cercle(3)
cer.info()
cer.aire()

