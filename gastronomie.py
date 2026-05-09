from flask import Flask, url_for
from app.lib.biblioteca_gastronomie import text_provenienta, text_ingrediente, text_preparare

app = Flask(__name__)

STYLE = """
<style>
    body {
        font-family: Arial, sans-serif;
        background: #fff8e7;
        margin: 0;
        padding: 0;
        text-align: center;
    }
    .card {
        background: #fffdf8;
        max-width: 750px;
        margin: 60px auto;
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #f3d9a4;
        box-shadow: 0 4px 20px rgba(180, 140, 80, 0.2);
    }
    h1 {
        margin-bottom: 15px;
        color: #c68b3f;
        font-size: 2.8em;
        text-shadow: 1px 1px 0 #fff;
    }
    .btn {
        display: inline-block;
        margin: 10px;
        padding: 12px 22px;
        border-radius: 25px;
        text-decoration: none;
        color: #4a2e0f;
        font-weight: bold;
        border: 2px solid transparent;
    }
    .btn-miere { background: #f7c873; }
    .btn-crem { background: #ffe9c7; }
    .btn-auriu { background: #f1b24a; }
    .btn-inchis { background: #d49a54; }
    .btn:hover {
        opacity: 0.85;
        border-color: #8b5e2b;
    }
    .text {
        margin-top: 20px;
        font-size: 1.15em;
        line-height: 1.6;
        color: #5a4630;
        text-align: justify;
    }
</style>
"""

def page(content):
    return STYLE + f"<div class='card'>{content}</div>"

@app.route('/')
def index():
    return "<script>window.location.href='/gastronomie';</script>"

@app.route("/gastronomie")
def gastronomie():
    image_url = url_for('static', filename='clatite.jpg')
    return page(f"""
        <h1>Clătite Americane</h1>

        <img src="{image_url}" alt="Clătite Americane"
             style="width:350px; border-radius:15px; margin:20px 0;">

        <div style="margin-top:25px;">
            <a class='btn btn-miere' href='/clatite/preparare'>Preparare</a>
            <a class='btn btn-crem' href='/clatite/ingrediente'>Ingrediente</a>
            <a class='btn btn-auriu' href='/clatite/origine'>Origine</a>
        </div>
    """)

@app.route('/clatite/preparare')
def preparare():
    return page(f"""
        <h1>Preparare</h1>
        <p class='text'>{text_preparare()}</p>
        <a class='btn btn-inchis' href='/gastronomie'>Înapoi</a>
    """)

@app.route('/clatite/origine')
def origine():
    return page(f"""
        <h1>Origine</h1>
        <p class='text'>{text_provenienta()}</p>
        <a class='btn btn-inchis' href='/gastronomie'>Înapoi</a>
    """)

@app.route('/clatite/ingrediente')
def ingrediente():
    return page(f"""
        <h1>Ingrediente</h1>
        <p class='text'>{text_ingrediente()}</p>
        <a class='btn btn-inchis' href='/gastronomie'>Înapoi</a>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
