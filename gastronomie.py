from flask import Flask
from app.lib.biblioteca_gastronomie import culoare_carbonara, descriere_carbonara

app = Flask(__name__)

@app.route('/gastronomie')
def tema():
    return "Tema: Gastronomie"

@app.route('/carbonara')
def element():
    return "Preparat: Paste Carbonara"

@app.route('/culoare_carbonara')
def culoare():
    return culoare_carbonara()

@app.route('/descriere_carbonara')
def descriere():
    return descriere_carbonara()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
