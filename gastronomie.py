from flask import Flask, render_template
from app.lib.biblioteca_gastronomie import descriere_brasovence, ingrediente_brasovence, tara_brasovence

app = Flask(__name__)

@app.route('/gastronomie')
def tema():
    return render_template('index.html')

@app.route('/tara_brasovence') # Aceasta este ruta pentru link-ul 1
def tara():
    return f"<h1>Locul de provenienta</h1><p>{tara_brasovence()}</p>"

@app.route('/ingrediente_brasovence')
def ingrediente():
    return f"<h1>Ingrediente</h1><p>{ingrediente_brasovence()}</p>"

@app.route('/descriere_brasovence')
def descriere():
    return f"<h1>Modul de preparare</h1><p>{descriere_brasovence()}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
