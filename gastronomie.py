from flask import Flask
from app.lib.biblioteca_gastronomie import reteta_mici, descriere_mici

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head><title>Gastronomie Romaneasca</title></head>
    <body>
        <h1>🍽️ Gastronomie Romaneasca</h1>
        <ul>
            <li><a href="/gastronomie">Gastronomie</a></li>
            <li><a href="/mici">Mici</a></li>
            <li><a href="/mici/reteta">Reteta Mici</a></li>
            <li><a href="/mici/descriere">Descriere Mici</a></li>
        </ul>
    </body>
    </html>
    '''

@app.route('/gastronomie')
def gastronomie():
    return '<h1>🍽️ Gastronomie Romaneasca</h1><p>Bine ati venit!</p><a href="/">Inapoi</a>'

@app.route('/mici')
def mici():
    return '<h1>🥩 Mici</h1><p>Preparatul traditional romanesc!</p><a href="/">Inapoi</a>'

@app.route('/mici/reteta')
def reteta():
    return f'<h1>📋 Reteta Mici</h1><p>{reteta_mici()}</p><a href="/">Inapoi</a>'

@app.route('/mici/descriere')
def descriere():
    return f'<h1>📖 Descriere Mici</h1><p>{descriere_mici()}</p><a href="/">Inapoi</a>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
