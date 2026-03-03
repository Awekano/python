#Faire un code qui permet à l'utilisateur de jouer à Pierre-Feuille-Ciseaux face à l'ordinateur (avec égalité possible) CORRECTION
import random

options = ["pierre", "feuille", "ciseaux"]
choix_bot = random.choice(options)
choix_utilisateur = input("pierre, feuille ou ciseaux : ")

if choix_utilisateur in options:
    if choix_utilisateur == choix_bot:
        print("Égalité (^_^;)")
    if choix_bot == "pierre" and choix_utilisateur == "ciseaux" or choix_bot == "ciseaux" and choix_utilisateur == "feuille" or choix_bot == "feuille" and choix_utilisateur == "pierre":
        print(f"Dommage tu as perdu le bot à choisi {choix_bot}")
    elif choix_bot == "pierre" and choix_utilisateur == "feuille" or choix_bot == "ciseaux" and choix_utilisateur == "pierre" or choix_bot == "feuille" and choix_utilisateur == "ciseaux":
        print(f"Gagné ! {choix_bot}")
else:
    print("Choix invalide")