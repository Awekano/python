class Personne():
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def afficher_infos(self):
        print(f"Infos : {self.prenom} {self.nom} {self.age}")

class Etudiant(Personne):
    pass

etudiant_n1 = Etudiant("BAYLE", "Enzo", 19)
etudiant_n1.afficher_infos()
