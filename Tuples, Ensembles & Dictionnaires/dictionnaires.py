#Les dictionnaires permettent de mettre des valeurs sur des clés par exemple la clé nom de la variable personne1 renvoie "BAYLE--SOCHELEAU"
#Cela fonctionne très bien avec le f-string par exemple
personne1 = {"nom" : "BAYLE--SOCHELEAU", "prenom" : "Enzo", "age" : 19}
print(personne1)

print(f"Bonjour je suis {personne1["nom"]} {personne1["prenom"]} et j'ai actuellement {personne1["age"]} ans")

#Il est possible de modifier la valeur d'une clé 
personne1["age"] = 20
print(f"Et là je viens d'avoir {personne1["age"]} ans")

#Il est possible de rajouter des clés dans un dictionnaires avec sa valeur
personne1["statut"] = "Etudiant" 
print(f"Je suis également {personne1['statut']}")

#Il est également possible de supprimer des clés sur les dictionnaires
del personne1["statut"]
