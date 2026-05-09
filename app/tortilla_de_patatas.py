from flask import Flask, render_template
from lib.biblioteca_tortilla import origine_tortilla, ingrediente_tortilla, preparare_tortilla

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/origine")
def origine():
    return render_template("origine.html", origine=origine_tortilla())

@app.route("/ingrediente")
def ingrediente():
    return render_template("ingrediente.html", ingrediente=ingrediente_tortilla())

@app.route("/preparare")
def preparare():
    return render_template("preparare.html", preparare=preparare_tortilla())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
