from flask import Flask
from app.lib.biblioteca_gastronomie import ingrediente_margherita, descriere_margherita

app = Flask(__name__)

@app.route('/')
def ruta_tema():
    return "Tema: Gastronomie"

@app.route('/margherita')
def ruta_element():
    return "Element: Margherita"

@app.route('/margherita/ingrediente')
def ruta_info1():
    return ingrediente_margherita()

@app.route('/margherita/descriere')
def ruta_info2():
    return descriere_margherita()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

