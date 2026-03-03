#En utilisant les tuples, ensembles ou dictionnaire faites un convertisseur d'unité CORRECTION
#L'utilisateur entrera une valeur en mètres et indiquera ensuite : km, mm ou cm (si il entre une unité autre cela renverra "Unité invalide") CORRECTION
#Et la convertion se fera par exemple : "Valeur en mètres " : 10, "Valeur souhaité (km, mm, cm) : " km, "Résultat : 0.01km" CORRECTION
convertisseur = {"km" : 0.001, "cm" : 100, "mm" : 1000}

distance_utilisateur = float(input("Entrez une distance en mètres : "))
unite_utilisateur = input("Entrez l'unité (km, cm, mm) : ")

if unite_utilisateur in convertisseur:
    print(f"La convertion de {distance_utilisateur}m en {unite_utilisateur} est de {distance_utilisateur*convertisseur[unite_utilisateur]}{unite_utilisateur}")
else:
    print("Unité invalide")