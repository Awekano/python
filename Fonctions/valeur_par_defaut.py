#Il est possible dans les fonctions d'affecter des valeurs par défaut dans les arguments de la fonction et de les remplacer si besoin
def message(prenom = "Enzo"):
    print(f"Bonjour {prenom}")

message()
message("Thibault")