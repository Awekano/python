#Création de méthodes de classe
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = None
    def afficher_infos(self):
        print(f"Infos : {self.prenom} {self.nom} {self.age} {self.email}")
    def changer_email(self, email):
        self.email = email
awekano = Personne("BAYLE--SOCHELEAU", "Enzo", 19)
awekano.afficher_infos()
awekano.changer_email("awekano@bitcoin.fr")
awekano.afficher_infos()