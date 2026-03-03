#Créer une fonction qui reprendra le code de l'exercice 'Tuples, Ensembles & Dictionnaires'/correction_conversion_unite.py 
convertisseur = {"km" : 0.001, "hm":0.01, "dam": 0.1, "m": 1, "dm" : 10, "cm" : 100, "mm" : 1000}

distance_utilisateur = float(input("Entrez une distance en mètres : "))
unite_utilisateur = input("Entrez l'unité (km, cm, mm) : ")

if unite_utilisateur in convertisseur:
    print(f"La conversion de {distance_utilisateur}m en {unite_utilisateur} est de {distance_utilisateur*convertisseur[unite_utilisateur]}{unite_utilisateur}")
else:
    print("Unité invalide")