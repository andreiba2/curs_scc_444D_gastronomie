from flask import Flask
from app.lib.biblioteca_gastronomie import reteta_mici, descriere_mici

app = Flask(__name__)

@app.route('/gastronomie')
def gastronomie():
    return "Bine ati venit la sectiunea de Gastronomie romaneasca!"

@app.route('/mici')
def mici():
    return "Pagina dedicata micilor - preparatul traditional romanesc!"

@app.route('/mici/reteta')
def reteta():
    return reteta_mici()

@app.route('/mici/descriere')
def descriere():
    return descriere_mici()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
