from flask import Flask, render_template_string
from app.lib.biblioteca_gastronomie import descriere_baklava, origine_baklava

app = Flask(__name__)

# CSS comun pentru Dark Mode aplicat pe toate rutele
DARK_MODE_STYLE = """
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        margin-top: 50px;
        background-color: #121212; /* Fundal Dark Mode */
        color: #e0e0e0; /* Text gri deschis */
    }
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
    <head>
        <title>Baklava</title>
        {DARK_MODE_STYLE}
    </head>
    <body>
        <h1>Element: Baklava</h1>
        <img src="https://img.magnific.com/premium-photo/turkish-havuc-dilim-baklava-with-pistachio-carrot-slice-baklava-black-background-top-view_89816-41102.jpg" alt="Baklava">
        <br>
        <a href="/baklava/descriere" class="btn">Vezi Descriere</a>
        <a href="/baklava/origine" class="btn">Vezi Origine</a>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/baklava/descriere')
def route_descriere_baklava():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Descriere Baklava</title>
        {DARK_MODE_STYLE}
    </head>
    <body>
        <h2>Descriere Baklava</h2>
        <p>{descriere_baklava()}</p>
        <a href='/baklava' class="back-link">⬅ Înapoi la meniu</a>
    </body>
    </html>
    """

@app.route('/baklava/origine')
def route_origine_baklava():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Origine Baklava</title>
        {DARK_MODE_STYLE}
    </head>
    <body>
        <h2>Origine Baklava</h2>
        <p>{origine_baklava()}</p>
        <a href='/baklava' class="back-link">⬅ Înapoi la meniu</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)