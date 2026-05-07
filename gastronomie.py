from flask import Flask
from app.lib.biblioteca_gastronomie import provenienta_margherita, ingrediente_margherita, preparare_margherita

app = Flask(__name__)

@app.route('/')
def ruta_tema():
    return "Tema: Gastronomie"

@app.route('/margherita')
def ruta_element():
    return "Element: Margherita"

@app.route('/margherita/provenienta')
def ruta_provenienta():
    return provenienta_margherita()

@app.route('/margherita/ingrediente')
def ruta_ingrediente():
    return ingrediente_margherita()

@app.route('/margherita/preparare')
def ruta_preparare():
    return preparare_margherita()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
