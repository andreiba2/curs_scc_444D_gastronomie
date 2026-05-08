from flask import Flask
from app.lib.biblioteca_gastronomie import descriere_baklava, origine_baklava

app = Flask(__name__)

# Cele 4 rute cerute
@app.route('/gastronomie')
def gastronomie():
    return "Tema: Gastronomie"

@app.route('/baklava')
def baklava():
    return "Element: Baklava"

@app.route('/baklava/descriere')
def route_descriere_baklava():
    return descriere_baklava()

@app.route('/baklava/origine')
def route_origine_baklava():
    return origine_baklava()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)