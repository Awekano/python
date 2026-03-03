#Déclaration d'une classe et d'un objet de cette dernière
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

awekano = Personne("BAYLE--SOCHELEAU", "Enzo", 19)
print(awekano.prenom, awekano.nom, awekano.age)