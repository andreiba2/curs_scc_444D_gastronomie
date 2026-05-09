from flask import Flask
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app.lib.biblioteca_gastronomie import origine_pizza, descriere_pizza

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html><head><title>Gastronomie 444D</title></head>
    <body>
        <h1>🍽️ Aplicatie Gastronomie - Grupa 444D</h1>
        <p>Bine ai venit! Alege o sectiune:</p>
        <ul>
            <li><a href="/gastronomie">Gastronomie (tema generala)</a></li>
            <li><a href="/pizza">Pizza (element specific)</a></li>
            <li><a href="/origine_pizza">Originea Pizza</a></li>
            <li><a href="/descriere_pizza">Descrierea Pizza</a></li>
        </ul>
    </body></html>
    '''

@app.route('/gastronomie')
def gastronomie():
    return '''
    <html><head><title>Gastronomie</title></head>
    <body>
        <h1>🍽️ Gastronomie</h1>
        <p>Gastronomia este arta si stiinta prepararii si consumului mancarurilor de calitate.
        Aceasta imbina traditia culinara cu inovatia, reflectand cultura si identitatea unui popor.</p>
        <h2>Elemente:</h2>
        <ul>
            <li><a href="/pizza">🍕 Pizza</a></li>
        </ul>
        <br><a href="/">⬅ Inapoi</a>
    </body></html>
    '''

@app.route('/pizza')
def pizza():
    return f'''
    <html><head><title>Pizza</title></head>
    <body>
        <h1>🍕 Pizza</h1>
        <h2>Origine:</h2>
        <p>{origine_pizza()}</p>
        <h2>Descriere:</h2>
        <p>{descriere_pizza()}</p>
        <br>
        <a href="/origine_pizza">📖 Detalii Origine</a> |
        <a href="/descriere_pizza">📝 Detalii Descriere</a> |
        <a href="/">⬅ Inapoi</a>
    </body></html>
    '''

@app.route('/origine_pizza')
def ruta_origine_pizza():
    return f'''
    <html><head><title>Originea Pizza</title></head>
    <body>
        <h1>📖 Originea Pizza</h1>
        <p>{origine_pizza()}</p>
        <br><a href="/pizza">⬅ Inapoi la Pizza</a>
    </body></html>
    '''

@app.route('/descriere_pizza')
def ruta_descriere_pizza():
    return f'''
    <html><head><title>Descrierea Pizza</title></head>
    <body>
        <h1>📝 Descrierea Pizza</h1>
        <p>{descriere_pizza()}</p>
        <br><a href="/pizza">⬅ Inapoi la Pizza</a>
    </body></html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
