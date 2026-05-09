from flask import Flask
from app.lib.biblioteca_gastronomie import get_descriere, get_origine, get_ingrediente, get_preparare

app = Flask(__name__)

def aplica_design(titlu, continut, arata_buton_inapoi=True):
    buton_inapoi = '<a href="/" class="back-link">🔙 Revino la meniul principal</a>' if arata_buton_inapoi else ''
    
    return f"""
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <title>{titlu}</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #fdf8f5; /* Culoare de fundal crem */
                color: #3b2818;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }}
            .card-reteta {{
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 10px 20px rgba(0,0,0,0.08);
                max-width: 600px;
                width: 100%;
                text-align: center;
            }}
            h1 {{
                color: #6e4c30;
                border-bottom: 2px solid #ecd3c0;
                padding-bottom: 10px;
            }}
            p {{
                font-size: 1.1em;
                line-height: 1.6;
                text-align: justify;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin: 15px 0;
            }}
            .btn-meniu {{
                display: block;
                background-color: #6e4c30;
                color: white;
                padding: 12px;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                transition: background 0.3s;
            }}
            .btn-meniu:hover {{
                background-color: #4a3320;
            }}
            .back-link {{
                display: inline-block;
                margin-top: 30px;
                color: #6e4c30;
                text-decoration: none;
                font-weight: bold;
                border: 2px solid #6e4c30;
                padding: 8px 15px;
                border-radius: 5px;
                transition: all 0.3s;
            }}
            .back-link:hover {{
                background-color: #6e4c30;
                color: white;
            }}
        </style>
    </head>
    <body>
        <div class="card-reteta">
            {continut}
            {buton_inapoi}
        </div>
    </body>
    </html>
    """

@app.route('/')
def home():
    continut = f"""
        <h1>Deliciul Italian: Tiramisu ☕</h1>
        <p><strong>Despre:</strong> {get_descriere()}</p>
        <h3 style="color: #8e6542; margin-top: 30px;">Află mai multe detalii:</h3>
        <ul>
            <li><a href="/tiramisu" class="btn-meniu">🌍 Origine și Istoric</a></li>
            <li><a href="/feature-1" class="btn-meniu">🛒 Ingrediente Necesare</a></li>
            <li><a href="/feature-2" class="btn-meniu">👨‍🍳 Mod de Preparare</a></li>
        </ul>
    """
    return aplica_design("Proiect Tiramisu - Acasa", continut, arata_buton_inapoi=False)

@app.route('/tiramisu')
def origine():
    continut = f"""
        <h1>Unde a apărut Tiramisu?</h1>
        <p>🌍 {get_origine()}</p>
    """
    return aplica_design("Origine Tiramisu", continut)

@app.route('/feature-1')
def ingrediente():
    continut = f"""
        <h1>Ce ne trebuie?</h1>
        <p>🛒 {get_ingrediente()}</p>
    """
    return aplica_design("Ingrediente Tiramisu", continut)

@app.route('/feature-2')
def preparare():
    continut = f"""
        <h1>Cum se face?</h1>
        <p>👨‍🍳 {get_preparare()}</p>
    """
    return aplica_design("Preparare Tiramisu", continut)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
