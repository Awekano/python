#Récupérer les initales d'un nom ou phrases
nom_complet = input("Nom complet : ")

nom_complet_split = nom_complet.split(" ")
initiales = nom_complet_split[0][0] + nom_complet_split[1][0]
initiales = initiales.upper()

print(f"Les initiales de {nom_complet} sont {initiales}")