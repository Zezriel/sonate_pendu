from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/play", methods=["GET","POST"])
def play():
    # La fonction play() peut à présent être employée avec une requpete GET (affichage classique dans le navigateur),
    # mais également pour les requêtes POST (envoi d'informations).
    player_name = ""
    if request.method == "POST":
        
        # On récupère les valeurs saisies dans le champ correspondant au name "mon_champ"
        player_name = request.form["player_name"]
        name_output = "Bienvenu"+player_name
        
        # Traitement
        # ...

    return render_template("play.html",name_output = name_output)


