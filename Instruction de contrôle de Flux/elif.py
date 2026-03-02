username = input("Pseudo : ")
users = ["Paul", "Enzo"]
admins = ["Awekano", "Enzo"]

if username in users:
    print("Bienvenue")
elif username in admins:
    print("Bienvenue ADMIN")
else:
    print("Erreur")