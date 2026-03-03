#Faire un code qui permet à l'utilisateur de jouer à Pierre-Feuille-Ciseaux face à l'ordinateur (avec égalité possible) CORRECTION
import random

options = ["pierre", "feuille", "ciseaux"]
choix_bot = random.choice(options)
choix_utilisateur = input("pierre, feuille ou ciseaux : ")

if choix_utilisateur in options:
    if choix_utilisateur == choix_bot:
        print("Égalité !")
    else:
        if choix_utilisateur == "pierre" and choix_bot == "ciseaux" or choix_utilisateur == "ciseaux" and choix_bot == "feuille" or choix_utilisateur == "feuille" and choix_bot == "pierre":
            print(f"Gagné !")
        else:
            print(f"Perdu !")