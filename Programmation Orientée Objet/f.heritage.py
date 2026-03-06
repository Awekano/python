class Personne():
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def afficher_infos(self):
        print(f"Infos : {self.prenom} {self.nom} {self.age}")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, notes):
        super().__init__(nom, prenom, age)
        self.notes = notes
    def afficher_infos(self):
        super().afficher_infos()
        print(f"Voici mes notes {self.notes}")

etudiant_n1 = Etudiant("BAYLE", "Enzo", 19, {"Mathématiques" : 15, "Anglais" : 19, "Informatique": 12})
etudiant_n1.afficher_infos()
