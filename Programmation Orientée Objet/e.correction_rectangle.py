#Créer la classe rectangle CORRECTION
#Créer méthode perimetre() qui calcul le perimètre du rectangle CORRECTION
#Créer méthode aire() qui calcul l'aire du rectangle CORRECTION
#Créer méthode est_carre() qui vérifie si le rectangle est un carré CORRECTION

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        print(f"Le périmètre du rectangle est de {2*(self.longueur*self.largeur)}")
    
    def aire(self):
        print(f"L'aire du rectangle est de {self.largeur*self.longueur}")
    
    def est_carre(self):
        if self.longueur == self.largeur:
            print("Il est carré")
        else:
            print("Il n'est pas carré")
        
rectangle_1 = Rectangle(15,5)
rectangle_1.perimetre()
rectangle_1.aire()
rectangle_1.est_carre()

rectangle_2 = Rectangle(5,5)
rectangle_2.perimetre()
rectangle_2.aire()
rectangle_2.est_carre()
