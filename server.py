from flask import Flask, render_template, request

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



    return render_template("play.html")


