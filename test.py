from random import randint
import os
from unidecode import unidecode

os.system("cls")
player_name = input('Entrer votre Nom: ')
os.system("cls")
print(f"Bienvenue {player_name}")

pendu = [
        """
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
          =========
        """,
        """
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
          =========
        """,
        """
            +---+
            |   |
            O   |
           /|\  |
                |
                |
          =========
        """,
        """
            +---+
            |   |
            O   |
            |   |
                |
                |
          =========
        """,
        """
            +---+
            |   |
            O   |
                |
                |
                |
          =========
        """,
        """
            +---+
            |   |
                |
                |
                |
                |
          =========
        """
    ]


dico = open("dictionnaire.txt", encoding="utf-8")
liste = dico.readlines()
dico.close()
rdm = randint(0,len(liste))
mot = liste[rdm].split(";")
mot = mot[0]
mot_decode = unidecode(mot)
vie = 5

liste_indice = []
for x in range(len(mot)):
    liste_indice.append("_") 
main = True
while main:
    indice = "".join(liste_indice)
    if "_" not in indice:
        print("Gagner!")
        break
    print(pendu[vie])
    print(indice)
    player_input = input("\n\nChoisisser une lettre: ")
    os.system("cls")
    if player_input in mot_decode:
        cherche = [pos for pos, char in enumerate(mot_decode) if char == player_input]
        for x in cherche:
            liste_indice[x] = mot[x]
    else:
        vie -= 1

    if vie == 0:
        print(pendu[0])
        print("Perdu!")
        break