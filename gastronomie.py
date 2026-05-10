from flask import Flask
from app.lib.biblioteca_gastronomie import provenienta_ramen, ingrediente_ramen, preparare_ramen

app = Flask(__name__)

CSS_STYLE = """
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #121212;
        color: #ffffff;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        text-align: center;
    }
    .container {
        background: #1e1e1e;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        max-width: 600px;
        width: 90%;
        border: 1px solid #333;
    }
    h1 {
        color: #ff6b6b;
        margin-bottom: 10px;
        font-size: 2.5em;
    }
    h2 {
        color: #4ecdc4;
        font-weight: 300;
        margin-bottom: 20px;
    }
    h3 {
        color: #a8a8a8;
        font-size: 1.1em;
        margin-bottom: 30px;
    }
    p {
        font-size: 1.2em;
        line-height: 1.6;
        color: #e0e0e0;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        margin: 15px 0;
    }
    a {
        display: inline-block;
        text-decoration: none;
        color: #ffffff;
        background: linear-gradient(135deg, #ff6b6b, #ff8e8b);
        padding: 12px 25px;
        border-radius: 25px;
        font-weight: bold;
        transition: transform 0.2s, box-shadow 0.2s;
        width: 80%;
        max-width: 300px;
    }
    a:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
    }
    .back-btn {
        background: transparent;
        border: 2px solid #ff6b6b;
        color: #ff6b6b;
        margin-top: 20px;
    }
    .back-btn:hover {
        background: #ff6b6b;
        color: #fff;
    }
</style>
"""

@app.route('/')
@app.route('/gastronomie')
def tema_gastronomie():
    return f'''
    <html>
    <head>
        <title>Tema Gastronomie</title>
        {CSS_STYLE}
    </head>
    <body>
        <div class="container">
            <h1>Tema proiectului: Gastronomie</h1>
            <h2>Student: Curca Andrei-Daniel | Grupa: 444D</h2>
            <p>Aceasta este ruta generală pentru tema grupei noastre.</p>
            <br>
            <a href="/ramen">Vezi proiectul meu (Ramen) 🍜</a>
        </div>
    </body>
    </html>
    '''
@app.route('/ramen')
def element_ramen():
    return f'''
    <html>
    <head>
        <title>Proiect Ramen</title>
        {CSS_STYLE}
    </head>
    <body>
        <div class="container">
            <h1>🍜 Ramen</h1>
            <p>Alege una dintre informațiile de mai jos:</p>
            <ul>
                <li><a href="/ramen/provenienta">📍 Locul de proveniență</a></li>
                <li><a href="/ramen/ingrediente">🥬 Ingrediente principale</a></li>
                <li><a href="/ramen/preparare">👨‍🍳 Modul de preparare</a></li>
            </ul>
            <br>
            <a href="/" class="back-btn">⬅️ Înapoi la pagina principală</a>
        </div>
    </body>
    </html>
    '''

@app.route('/ramen/provenienta')
def afisare_provenienta():
    rezultat = provenienta_ramen()
    return f'''
    <html>
    <head>
        <title>Provenienta Ramen</title>
        {CSS_STYLE}
    </head>
    <body>
        <div class="container">
            <h2>📍 Locul de proveniență</h2>
            <p>{rezultat}</p>
            <a href="/ramen" class="back-btn">⬅️ Înapoi la meniul Ramen</a>
        </div>
    </body>
    </html>
    '''

@app.route('/ramen/ingrediente')
def afisare_ingrediente():
    rezultat = ingrediente_ramen()
    return f'''
    <html>
    <head>
        <title>Ingrediente Ramen</title>
        {CSS_STYLE}
    </head>
    <body>
        <div class="container">
            <h2>🥬 Ingrediente principale</h2>
            <p>{rezultat}</p>
            <a href="/ramen" class="back-btn">⬅️ Înapoi la meniul Ramen</a>
        </div>
    </body>
    </html>
    '''

@app.route('/ramen/preparare')
def afisare_preparare():
    rezultat = preparare_ramen()
    return f'''
    <html>
    <head>
        <title>Preparare Ramen</title>
        {CSS_STYLE}
    </head>
    <body>
        <div class="container">
            <h2>👨‍🍳 Modul de preparare</h2>
            <p>{rezultat}</p>
            <a href="/ramen" class="back-btn">⬅️ Înapoi la meniul Ramen</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

