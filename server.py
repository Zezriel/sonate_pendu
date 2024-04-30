from flask import Flask, render_template, request
from random import randint
from unidecode import unidecode

app = Flask(__name__)


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
indice = "".join(liste_indice)




@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        
        global player_name
        player_name = request.form["player_name"]
        
        
        return render_template("play.html")
    return render_template("home.html")





@app.route("/play", methods=["GET","POST"])
def play():



    return render_template("play.html",indice = indice)



@app.route('/button_click', methods=["GET",'POST'])
def button_click():
    letter = request.form["letter"]
    print(letter)
    return render_template("play.html",indice = indice)




