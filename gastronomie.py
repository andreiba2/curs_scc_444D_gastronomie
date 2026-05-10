from flask import Flask
# Importăm cele 3 funcții noi din bibliotecă
from app.lib.biblioteca_gastronomie import origine_macarons, ingrediente_macarons, preparare_macarons

app = Flask(__name__)

# 1. Ruta pentru temă (Gastronomie) 
@app.route('/gastronomie')
def gastronomie():
    return """
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #fdf6f5;">
            <h1 style="color: #d17b9b;">🍽️ Proiect SCC: Gastronomie</h1>
            <p style="font-size: 1.2em; color: #4a3b3f;">Tema: Grupa 444D</p>
            <hr style="width: 50%; margin: 20px auto; border-color: #f5e1e6;">
            <a href="/macarons" style="text-decoration: none; font-weight: bold; color: #d17b9b; font-size: 1.1em; padding: 10px 20px; border: 2px solid #d17b9b; border-radius: 20px;">
                ➔ Mergi la Elementul Specific: Macarons
            </a>
        </body>
    </html>
    """

# 2. Ruta pentru elementul specific (Macarons)
@app.route('/macarons')
def macarons():
    return """
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #fdf6f5;">
            <h1 style="color: #d17b9b;">✨ Element: Macarons</h1>
            <p style="font-size: 1.1em; color: #4a3b3f;">O bijuterie a cofetăriei franțuzești, crocantă la exterior și moale la interior.</p>
            
            <div style="margin-top: 40px; display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
                <a href="/origine_macarons" style="padding: 15px 25px; background: #f4d03f; color: #4a3b3f; border-radius: 25px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    🌍 Țara/Locul de proveniență
                </a>
                <a href="/ingrediente_macarons" style="padding: 15px 25px; background: #8db596; color: white; border-radius: 25px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    📋 Ingrediente principale
                </a>
                <a href="/preparare_macarons" style="padding: 15px 25px; background: #af7ac5; color: white; border-radius: 25px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    👩‍🍳 Mod de preparare
                </a>
            </div>
            
            <br><br><br>
            <a href="/gastronomie" style="color: #a09296; text-decoration: none;">« Înapoi la Pagina de Temă</a>
        </body>
    </html>
    """

# 3. Ruta pentru informația 1: Origine
@app.route('/origine_macarons')
def ruta_origine():
    continut = origine_macarons()
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 40px; background-color: #fdf6f5; line-height: 1.6;">
            <div style="max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                <h2 style="color: #d35400; border-bottom: 2px solid #f4d03f; padding-bottom: 10px;">🌍 Țara și Locul de Proveniență</h2>
                <p style="font-size: 1.1em; color: #4a3b3f;">{continut}</p>
                <br>
                <a href="/macarons" style="color: #d35400; text-decoration: none; font-weight: bold;">⬅ Înapoi la Macarons</a>
            </div>
        </body>
    </html>
    """

# 4. Ruta pentru informația 2: Ingrediente
@app.route('/ingrediente_macarons')
def ruta_ingrediente():
    continut = ingrediente_macarons()
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 40px; background-color: #fdf6f5;">
            <div style="max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                <h2 style="color: #27ae60; border-bottom: 2px solid #8db596; padding-bottom: 10px;">📋 Ingrediente Principale</h2>
                <div style="font-size: 1.1em; padding: 15px; border-left: 5px solid #8db596; background: #f4fbf6; color: #4a3b3f;">
                    {continut}
                </div>
                <br>
                <a href="/macarons" style="color: #27ae60; text-decoration: none; font-weight: bold;">⬅ Înapoi la Macarons</a>
            </div>
        </body>
    </html>
    """

# 5. Ruta pentru informația 3: Preparare
@app.route('/preparare_macarons')
def ruta_preparare():
    continut = preparare_macarons()
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 40px; background-color: #fdf6f5; line-height: 1.6;">
            <div style="max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                <h2 style="color: #8e44ad; border-bottom: 2px solid #af7ac5; padding-bottom: 10px;">👩‍🍳 Mod de Preparare</h2>
                <p style="font-size: 1.1em; color: #4a3b3f;">{continut}</p>
                <br>
                <a href="/macarons" style="color: #8e44ad; text-decoration: none; font-weight: bold;">⬅ Înapoi la Macarons</a>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    # Aplicația rulează pe portul 5000, accesibil din exteriorul containerului
    app.run(host='0.0.0.0', port=5000)
