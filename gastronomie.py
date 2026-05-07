from flask import Flask
from app.lib.biblioteca_gastronomie import descriere_cordon_bleu, origine_cordon_bleu

app = Flask(__name__)


@app.route('/gastronomie')
def gastronomie():
    return "Bine ai venit la pagina de Gastronomie!"


@app.route('/cordon_bleu')
def cordon_bleu():
    return "Element ales: Cordon Bleu"


@app.route('/cordon_bleu/descriere')
def descriere():
    return descriere_cordon_bleu()


@app.route('/cordon_bleu/origine')
def origine():
    return origine_cordon_bleu()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
