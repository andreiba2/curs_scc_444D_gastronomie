from flask import Flask
from app.lib.biblioteca_gastronomie import ingrediente_ramen, descriere_ramen

app = Flask(__name__)

@app.route('/gastronomie')
def tema_gastronomie():
    return "Tema proiectului este: Gastronomie"


@app.route('/ramen')
def element_ramen():
    return "Elementul ales este: Ramen"


@app.route('/ramen/ingrediente')
def afisare_ingrediente():
    return ingrediente_ramen()

@app.route('/ramen/descriere')
def afisare_descriere():
    return descriere_ramen()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
