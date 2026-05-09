from flask import Flask
from app.lib.biblioteca_gastronomie import descriere_ratatouille, origine_ratatouille

app = Flask(__name__)

STYLE = """
<style>
    body {
        font-family: Arial, sans-serif;
        background: #f4f4f4;
        margin: 0;
        padding: 0;
        text-align: center;
    }
    .card {
        background: white;
        max-width: 700px;
        margin: 80px auto;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    h1 {
        margin-bottom: 20px;
    }
    img {
        max-width: 550px;
        max-height: 412px;
        border-radius: 10px; 
        margin-top: 10px;
        margin-bottom: 20px; 
        box-shadow: 0 4px 8px rgba(255,255,255,0.1);
    }
    .btn {
        display: inline-block;
        margin: 10px;
        padding: 12px 22px;
        border-radius: 25px;
        text-decoration: none;
        color: white;
        font-weight: bold;
    }
    .btn-gastro { background: #333; }
    .btn-rosu { background: #c0392b; width: 200px; }
    .btn-verde { background: #27ae60; width: 200px; }
    .btn-galben { background: #f1c40f; color: #000; }
    .btn-mov { background: #8e44ad; }
    .text {
        margin-top: 20px;
        font-size: 1em;
    }
</style>
"""

def page(content):
    return STYLE + f"<div class='card'>{content}</div>"

@app.route('/gastronomie')
def gastronomie():
    return page("""
        <h1>Gastronomie</h1>
        <p class='text'>Bine ai venit in bucataria noastra!</p>
        <a class='btn btn-gastro' href='/ratatouille'>Descopera Ratatouille</a>
    """)

@app.route('/ratatouille')
def ratatouille():
    return page("""
        <h1>Ratatouille<h1>
        <img src="https://images.ctfassets.net/0e6jqcgsrcye/4teTkS26yJgQ4N30ofmyhX/33d2415ad06349ebb7ec030afdfc1db8/summerratatouille_thumbnail.webp" alt="Ratatouille image">
        <p class='text'>Afla mai multe despre acest preparat:</p>
        <a class='btn btn-rosu' href='/ratatouille/descriere'>Descriere</a>
        <a class='btn btn-verde' href='/ratatouille/origine'>Origine</a>
        <br><br>
        <a class='btn btn-galben' href='/gastronomie'>Inapoi</a>
    """)

@app.route('/ratatouille/descriere')
def route_descriere_ratatouille():
    return page(f"""
        <h1 style='color:#c0392b;'>Descriere</h1>
        <p class='text'>{descriere_ratatouille()}</p>
        <a class='btn btn-mov' href='/ratatouille'>Înapoi</a>
    """)

@app.route('/ratatouille/origine')
def route_origine_ratatouille():
    return page(f"""
        <h1 style='color:#27ae60;'>Origine</h1>
        <p class='text'>{origine_ratatouille()}</p>
        <a class='btn btn-mov' href='/ratatouille'>Înapoi</a>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
