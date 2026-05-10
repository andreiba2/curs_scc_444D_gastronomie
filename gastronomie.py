from flask import Flask, render_template_string
from app.lib.biblioteca_gastronomie import provenienta_baklava, ingrediente_baklava, preparare_baklava

app = Flask(__name__)

DARK_MODE_STYLE = """
<style>
    body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #121212; color: #e0e0e0; }
    img { max-width: 600px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(255,255,255,0.1); }
    .btn { display: inline-block; padding: 10px 20px; margin: 10px; background-color: #e67e22; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; }
    .btn:hover { background-color: #d35400; }
    a.back-link { color: #e67e22; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 20px;}
</style>
"""

@app.route('/gastronomie')
def gastronomie():
    return f"<html><head>{DARK_MODE_STYLE}</head><body><h1>Tema: Gastronomie</h1></body></html>"

@app.route('/baklava')
def baklava():
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Baklava</title>{DARK_MODE_STYLE}</head>
    <body>
        <h1>Element: Baklava</h1>
        <img src="https://img.magnific.com/premium-photo/turkish-havuc-dilim-baklava-with-pistachio-carrot-slice-baklava-black-background-top-view_89816-41102.jpg" alt="Baklava">
        <br>
        <a href="/baklava/provenienta" class="btn">Tara/locul de provenienta</a>
        <a href="/baklava/ingrediente" class="btn">Ingrediente principale</a>
        <a href="/baklava/preparare" class="btn">Modul de preparare</a>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/baklava/provenienta')
def route_provenienta():
    return f"<html><head><title>Proveniență</title>{DARK_MODE_STYLE}</head><body><h2>Țara/locul de proveniență</h2><p>{provenienta_baklava()}</p><a href='/baklava' class='back-link'>⬅ Înapoi la meniu</a></body></html>"

@app.route('/baklava/ingrediente')
def route_ingrediente():
    return f"<html><head><title>Ingrediente</title>{DARK_MODE_STYLE}</head><body><h2>Ingrediente principale</h2><p>{ingrediente_baklava()}</p><a href='/baklava' class='back-link'>⬅ Înapoi la meniu</a></body></html>"

@app.route('/baklava/preparare')
def route_preparare():
    return f"<html><head><title>Preparare</title>{DARK_MODE_STYLE}</head><body><h2>Modul de preparare</h2><p>{preparare_baklava()}</p><a href='/baklava' class='back-link'>⬅ Înapoi la meniu</a></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)