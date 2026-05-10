from flask import Flask
from app.lib.biblioteca_gastronomie import origine_piftie, ingrediente_piftie, preparare_piftie

app = Flask(__name__)

@app.route('/gastronomie')
def gastronomie():
    return """
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #f8f9fa;">
            <h1 style="color: #d35400;">Proiect SCC: Gastronomie</h1>
            <p style="font-size: 1.2em;">Tema: Grupa 444D</p>
            <hr style="width: 50%; margin: 20px auto;">
            <a href="/piftie" style="text-decoration: none; font-weight: bold; color: #2980b9; font-size: 1.1em;">
                ➔ Mergi la Elementul Specific: Piftie
            </a>
        </body>
    </html>
    """

@app.route('/piftie')
def piftie():
    return """
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #f8f9fa;">
            <h1 style="color: #2c3e50;">Element: Piftie</h1>
            <p style="font-size: 1.1em;">Alege o caracteristică pentru a afla mai multe detalii:</p>
            <div style="margin-top: 30px;">
                <a href="/origine_piftie" style="padding: 15px 25px; background: #8e44ad; color: white; border-radius: 5px; text-decoration: none; margin-right: 10px; display: inline-block;">
                    🌍 Proveniență
                </a>
                <a href="/ingrediente_piftie" style="padding: 15px 25px; background: #27ae60; color: white; border-radius: 5px; text-decoration: none; margin-right: 10px; display: inline-block;">
                    📋 Ingrediente
                </a>
                <a href="/preparare_piftie" style="padding: 15px 25px; background: #2980b9; color: white; border-radius: 5px; text-decoration: none; display: inline-block;">
                    👨‍🍳 Preparare
                </a>
            </div>
            <br><br>
            <a href="/gastronomie" style="color: #7f8c8d; text-decoration: none;">« Înapoi la Pagina de Temă</a>
        </body>
    </html>
    """

@app.route('/origine_piftie')
def ruta_origine():
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 40px; background-color: #f8f9fa;">
            <div style="max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <h2 style="color: #8e44ad; border-bottom: 2px solid #8e44ad; padding-bottom: 10px;">Țara / Locul de Proveniență</h2>
                <p style="font-size: 1.1em;">{origine_piftie()}</p>
                <br>
                <a href="/piftie" style="color: #8e44ad; text-decoration: none; font-weight: bold;">⬅ Înapoi la Piftie</a>
            </div>
        </body>
    </html>
    """

@app.route('/ingrediente_piftie')
def ruta_ingrediente():
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 40px; background-color: #f8f9fa;">
            <div style="max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <h2 style="color: #27ae60; border-bottom: 2px solid #27ae60; padding-bottom: 10px;">Ingrediente Principale</h2>
                <p style="font-size: 1.1em;">{ingrediente_piftie()}</p>
                <br>
                <a href="/piftie" style="color: #27ae60; text-decoration: none; font-weight: bold;">⬅ Înapoi la Piftie</a>
            </div>
        </body>
    </html>
    """

@app.route('/preparare_piftie')
def ruta_preparare():
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 40px; background-color: #f8f9fa; line-height: 1.6;">
            <div style="max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <h2 style="color: #2980b9; border-bottom: 2px solid #2980b9; padding-bottom: 10px;">Modul de Preparare</h2>
                <p style="font-size: 1.1em;">{preparare_piftie()}</p>
                <br>
                <a href="/piftie" style="color: #2980b9; text-decoration: none; font-weight: bold;">⬅ Înapoi la Piftie</a>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
