from flask import Flask
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app.lib.biblioteca_gastronomie import origine_pizza, descriere_pizza

app = Flask(__name__)

STYLE = """
<style>
    body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; background: #f5f5f5; }
    h1 { color: #c0392b; border-bottom: 2px solid #c0392b; padding-bottom: 10px; }
    h2 { color: #e74c3c; }
    p { line-height: 1.6; color: #333; }
    a { color: #c0392b; text-decoration: none; font-weight: bold; }
    a:hover { text-decoration: underline; }
    ul { list-style: none; padding: 0; }
    ul li { margin: 10px 0; }
    ul li a { background: #c0392b; color: white; padding: 10px 20px; border-radius: 5px; display: inline-block; }
    ul li a:hover { background: #e74c3c; text-decoration: none; }
    .back { margin-top: 20px; display: inline-block; }
</style>
"""

@app.route('/')
def index():
    return f"""
    <html><head><title>Gastronomie 444D</title></head>
    <body>
    {STYLE}
        <h1>🍽️ Aplicatie Gastronomie - Grupa 444D</h1>
        <p>Bine ai venit! Alege o sectiune:</p>
        <ul>
            <li><a href="/gastronomie">🍽️ Gastronomie</a></li>
            <li><a href="/pizza">🍕 Pizza</a></li>
            <li><a href="/origine_pizza">📖 Originea Pizza</a></li>
            <li><a href="/descriere_pizza">📝 Descrierea Pizza</a></li>
        </ul>
    </body></html>
    """

@app.route('/gastronomie')
def gastronomie():
    return f"""
    <html><head><title>Gastronomie</title></head>
    <body>
    {STYLE}
        <h1>🍽️ Gastronomie</h1>
        <p>Gastronomia este arta si stiinta prepararii si consumului mancarurilor de calitate.
        Aceasta imbina traditia culinara cu inovatia, reflectand cultura si identitatea unui popor.</p>
        <h2>Elemente:</h2>
        <ul>
            <li><a href="/pizza">🍕 Pizza</a></li>
        </ul>
        <a class="back" href="/">⬅ Inapoi</a>
    </body></html>
    """

@app.route('/pizza')
def pizza():
    return f"""
    <html><head><title>Pizza</title></head>
    <body>
    {STYLE}
        <h1>🍕 Pizza</h1>
        <h2>Origine</h2>
        <p>{origine_pizza()}</p>
        <h2>Descriere</h2>
        <p>{descriere_pizza()}</p>
        <ul>
            <li><a href="/origine_pizza">📖 Detalii Origine</a></li>
            <li><a href="/descriere_pizza">📝 Detalii Descriere</a></li>
        </ul>
        <a class="back" href="/">⬅ Inapoi</a>
    </body></html>
    """

@app.route('/origine_pizza')
def ruta_origine_pizza():
    return f"""
    <html><head><title>Originea Pizza</title></head>
    <body>
    {STYLE}
        <h1>📖 Originea Pizza</h1>
        <p>{origine_pizza()}</p>
        <a class="back" href="/pizza">⬅ Inapoi la Pizza</a>
    </body></html>
    """

@app.route('/descriere_pizza')
def ruta_descriere_pizza():
    return f"""
    <html><head><title>Descrierea Pizza</title></head>
    <body>
    {STYLE}
        <h1>📝 Descrierea Pizza</h1>
        <p>{descriere_pizza()}</p>
        <a class="back" href="/pizza">⬅ Inapoi la Pizza</a>
    </body></html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
