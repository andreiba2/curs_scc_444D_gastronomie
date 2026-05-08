from flask import Flask
from app.lib.biblioteca_gastronomie import descriere_macarons, ingrediente_macarons

app = Flask(__name__)

@app.route('/gastronomie')
def gastronomie():
    return "Tema: Gastronomie"

@app.route('/macarons')
def macarons():
    return "Element: Macarons"

@app.route('/descriere_macarons')
def ruta_descriere():
    return descriere_macarons()

@app.route('/ingrediente_macarons')
def ruta_ingrediente():
    return ingrediente_macarons()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
