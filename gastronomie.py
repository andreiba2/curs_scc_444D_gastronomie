from flask import Flask
from app.lib.biblioteca_gastronomie import provenienta_margherita, ingrediente_margherita, preparare_margherita

app = Flask(__name__)

# Stil comun pentru butoane (pentru un aspect mai plăcut în screenshot)
stil_butoane = """
<style>
    .button {
        background-color: #4CAF50; border: none; color: white;
        padding: 15px 32px; text-align: center; text-decoration: none;
        display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;
        border-radius: 8px;
    }
</style>
"""

@app.route('/')
def ruta_tema():
    return "<h1>Tema: Gastronomie</h1><a href='/margherita'>Mergi la Margherita</a>"

@app.route('/margherita')
def ruta_element():
    return f"""
    {stil_butoane}
    <h1>Pagina Margherita</h1>
    <p>Alege ce vrei să afli despre Pizza Margherita:</p>
    <a href="/margherita/provenienta" class="button">Vezi Proveniența</a>
    <a href="/margherita/ingrediente" class="button">Vezi Ingrediente</a>
    <a href="/margherita/preparare" class="button">Vezi Preparare</a>
    """

@app.route('/margherita/provenienta')
def ruta_provenienta():
    return f"{provenienta_margherita()}<br><br><a href='/margherita'>Înapoi</a>"

@app.route('/margherita/ingrediente')
def ruta_ingrediente():
    return f"{ingrediente_margherita()}<br><br><a href='/margherita'>Înapoi</a>"

@app.route('/margherita/preparare')
def ruta_preparare():
    return f"{preparare_margherita()}<br><br><a href='/margherita'>Înapoi</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
