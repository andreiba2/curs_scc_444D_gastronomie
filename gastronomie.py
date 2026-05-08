from flask import Flask
from app.lib.biblioteca_gastronomie import ingrediente_clatite, descriere_clatite

app = Flask(__name__)

@app.route("/")
def tema():
    return "Tema: Gastronomie"

@app.route("/clatite")
def element():
    return "Element ales: Clătite americane"

@app.route("/clatite/ingrediente")
def route_ingrediente():
    return ingrediente_clatite()

@app.route("/clatite/descriere")
def route_descriere():
    return descriere_clatite()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
