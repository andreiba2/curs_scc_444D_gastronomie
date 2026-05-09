from flask import Flask
from app.lib.biblioteca_gastronomie import descriere_macarons, ingrediente_macarons

app = Flask(__name__)

CSS_TEMPLATE = """
<style>
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        background-color: #fcf4f6; /* Roz pastelat deschis */
        color: #4a3b3f; /* Maro închis/Cacao pentru text */
        text-align: center;
        padding: 40px 20px;
        margin: 0;
    }
    .card {
        background: white;
        max-width: 600px;
        margin: 0 auto;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    }
    h1 {
        color: #d17b9b; /* Roz macaron */
        margin-bottom: 5px;
    }
    h2 {
        color: #8db596; /* Verde fistic */
        border-bottom: 2px dashed #eee;
        padding-bottom: 15px;
    }
    .subtitle {
        font-size: 1.2em;
        color: #7a6a6e;
        margin-bottom: 30px;
    }
    .btn-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 30px;
    }
    .btn {
        padding: 12px 24px;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.3s ease;
        display: inline-block;
    }
    .btn-pistachio {
        background-color: #a3c9ac;
        color: white;
    }
    .btn-pistachio:hover { background-color: #8db596; box-shadow: 0 4px 10px rgba(163, 201, 172, 0.4); }
    
    .btn-berry {
        background-color: #d17b9b;
        color: white;
    }
    .btn-berry:hover { background-color: #b86281; box-shadow: 0 4px 10px rgba(209, 123, 155, 0.4); }
    
    .btn-back {
        background-color: transparent;
        color: #a09296;
        border: 2px solid #e8dadd;
        margin-top: 30px;
    }
    .btn-back:hover { background-color: #e8dadd; color: #4a3b3f; }
    
    .content-box {
        background: #fcfafb;
        border-radius: 12px;
        padding: 20px;
        font-size: 1.1em;
        line-height: 1.6;
        border-left: 5px solid #d17b9b;
        text-align: left;
    }
</style>
"""

@app.route('/gastronomie')
def gastronomie():
    return f"""
    <html>
        <head>{CSS_TEMPLATE}</head>
        <body>
            <div class="card">
                <h1>🍽️ Proiect SCC: Gastronomie</h1>
                <p class="subtitle">Tema: Grupa 444D</p>
                <div class="btn-container">
                    <a href="/macarons" class="btn btn-berry">➔ Mergi la Elementul Specific: Macarons</a>
                </div>
            </div>
        </body>
    </html>
    """

@app.route('/macarons')
def macarons():
    return f"""
    <html>
        <head>{CSS_TEMPLATE}</head>
        <body>
            <div class="card">
                <h1>✨ Element: Macarons</h1>
                <p class="subtitle">O bijuterie a cofetăriei franțuzești, crocantă și delicioasă.</p>
                <div class="btn-container">
                    <a href="/ingrediente_macarons" class="btn btn-pistachio">📋 Vezi Ingrediente</a>
                    <a href="/descriere_macarons" class="btn btn-berry">👩‍🍳 Descriere & Preparare</a>
                </div>
                <br>
                <a href="/gastronomie" class="btn btn-back">« Înapoi la Pagina de Temă</a>
            </div>
        </body>
    </html>
    """

@app.route('/descriere_macarons')
def ruta_descriere():
    continut = descriere_macarons()
    return f"""
    <html>
        <head>{CSS_TEMPLATE}</head>
        <body>
            <div class="card">
                <h2>📖 Descriere & Preparare</h2>
                <div class="content-box" style="border-left-color: #8db596;">
                    {continut}
                </div>
                <div class="btn-container">
                    <a href="/macarons" class="btn btn-back">⬅ Înapoi la Macarons</a>
                </div>
            </div>
        </body>
    </html>
    """

@app.route('/ingrediente_macarons')
def ruta_ingrediente():
    continut = ingrediente_macarons()
    return f"""
    <html>
        <head>{CSS_TEMPLATE}</head>
        <body>
            <div class="card">
                <h2 style="color: #d17b9b;">🛒 Ingrediente Necesare</h2>
                <div class="content-box">
                    {continut}
                </div>
                <div class="btn-container">
                    <a href="/macarons" class="btn btn-back">⬅ Înapoi la Macarons</a>
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
