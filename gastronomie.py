from flask import Flask
from app.lib.biblioteca_gastronomie import descriere_piftie, ingrediente_piftie

app = Flask(__name__)

@app.route('/gastronomie')
def gastronomie():
    return "Tema: Gastronomie"

@app.route('/piftie')
def piftie():
    return "Element: Piftie"
 
@app.route('/descriere_piftie')
def ruta_descriere():
    return descriere_piftie()

@app.route('/ingrediente_piftie')
def ruta_ingrediente():
    return ingrediente_piftie()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
