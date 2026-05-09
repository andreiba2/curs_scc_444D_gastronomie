from flask import Flask
from app.lib.biblioteca_gastronomie import ingrediente_ciorba_de_burta, descriere_ciorba_de_burta

app = Flask(__name__)

@app.route('/gastronomie')
def tema_gastronomie():
    return "Tema proiectului este: Gastronomie"

@app.route('/ciorba_de_burta')
def element_ramen():
    return "Elementul ales este: Ciorba de burta"

@app.route('/ciorba_de_burta/ingrediente')
def afisare_ingrediente():
    return ingrediente_ciorba_de_burta()

@app.route('/ciorba_de_burta/descriere')
def afisare_descriere():
    return descriere_ciorba_de_burta()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
