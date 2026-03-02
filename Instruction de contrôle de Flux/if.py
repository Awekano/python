#La fonction if permet de mettre des conditions en fonctions des données des variables et ou des entrées utilisateurs
username = input("Entre ton pseudo : ")
users = ["Yarus","Awekano","X-Traillus","Dimony","Artorias_LBL","Pascha_LBL","JuJu"]
if username in users:
    print("Salut", username)
else:
    print("Qui es tu", username,"?")