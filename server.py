from flask import Flask, render_template, request
from random import randint
from unidecode import unidecode

app = Flask(__name__)







@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        
        global player_name
        player_name = request.form["player_name"]

        
        
        return render_template("play.html")
    return render_template("home.html")






@app.route("/play", methods=["GET","POST"])
def play():



    if request.method == "GET":
        dico = open("dictionnaire.txt", encoding="utf-8")
        liste = dico.readlines()
        dico.close()
        rdm = randint(0,len(liste))
        global mot
        mot = liste[rdm].split(";")
        mot = mot[0]
        global mot_decode
        mot_decode = unidecode(mot)
        global vie
        vie = 5
        global liste_indice
        liste_indice = []
        for x in range(len(mot)):
            liste_indice.append("_")
        global indice
        indice = "".join(liste_indice)
        return render_template("play.html",indice = indice, vie = vie)
        

    if request.method == "POST":
        player_input = request.form["letter"]
        if player_input in mot_decode:
            cherche = [pos for pos, char in enumerate(mot_decode) if char == player_input]
            for x in cherche:

                liste_indice[x] = mot[x]
            indice = "".join(liste_indice)
        else:

            vie -= 1
        if vie <= 0:
            return render_template("end.html",vie = vie, mot = mot,message_fin = "Perdu!")
        
        if "_" not in indice:
            return render_template("end.html",vie = vie, mot = mot,message_fin = "Gagner!")
        return render_template("play.html",indice = indice, vie = vie)
    


