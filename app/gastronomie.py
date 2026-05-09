from flask import Flask, render_template

from app.lib.biblioteca_gastronomie import (
    origine,
    ingrediente,
    preparare,
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gastronomie")
def gastronomie():
    return render_template("index.html")


@app.route("/gastronomie/sushi")
def sushi():
    return render_template("index.html")


@app.route("/origine")
def pagina_origine():
    return render_template(
        "origine.html",
        titlu="Țara de proveniență",
        continut=origine()
    )


@app.route("/ingrediente")
def pagina_ingrediente():
    return render_template(
        "ingrediente.html",
        titlu="Ingrediente principale",
        continut=ingrediente()
    )


@app.route("/preparare")
def pagina_preparare():
    return render_template(
        "preparare.html",
        titlu="Modul de preparare",
        continut=preparare()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
