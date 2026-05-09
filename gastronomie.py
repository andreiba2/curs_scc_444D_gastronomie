from flask import Flask
from app.lib.biblioteca_gastronomie import descriere_salata_boeuf, ingrediente_salata_boeuf

app = Flask(__name__)

@app.route('/gastronomie')
def gastronomie():
    return "Tema: Gastronomie - Grupa 444D"

@app.route('/salata_boeuf')
def salata_boeuf():
    return "Element: Salata de Boeuf"

@app.route('/descriere_salata_boeuf')
def ruta_descriere():
    return descriere_salata_boeuf()

@app.route('/ingrediente_salata_boeuf')
def ruta_ingrediente():
    return ingrediente_salata_boeuf()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
