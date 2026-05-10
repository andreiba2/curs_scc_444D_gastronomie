from flask import Flask
from app.lib.biblioteca_gastronomie import ingrediente_ciorba_de_burta, descriere_ciorba_de_burta, preparare_ciorba_de_burta

app = Flask(__name__)

STYLE = '''
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #fdfaf6; color: #444; margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
    .container { background: #fff; padding: 40px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); width: 90%; max-width: 600px; text-align: center; border-top: 5px solid #e67e22; }
    h1 { color: #d35400; margin-bottom: 5px; }
    h2 { color: #7f8c8d; font-weight: 400; margin-bottom: 30px; }
    h3 { font-size: 0.9em; color: #95a5a6; }
    ul { list-style: none; padding: 0; }
    li { margin: 15px 0; }
    a { text-decoration: none; color: #fff; background: #e67e22; padding: 12px 25px; border-radius: 25px; display: inline-block; transition: 0.3s; font-weight: bold; }
    a:hover { background: #d35400; transform: translateY(-2px); box-shadow: 0 5px 15px rgba(211, 84, 0, 0.3); }
    .back-btn { background: #7f8c8d; margin-top: 20px; font-size: 0.9em; }
    .back-btn:hover { background: #2c3e50; }
    p { line-height: 1.6; text-align: justify; color: #555; }
</style>
'''

def wrap_html(content, back_link=False):
    """Funcție care împachetează conținutul în stilul vizual definit."""
    button = f'<br><a href="/" class="back-btn">⬅ Înapoi la meniu</a>' if back_link else ""
    return f'''
    <!DOCTYPE html>
    <html>
    <head><title>Proiect Gastronomie</title>{STYLE}</head>
    <body>
        <div class="container">
            {content}
            {button}
        </div>
    </body>
    </html>
    '''

@app.route('/')
def meniu_principal():
    content = '''
    <h1>Ciorbă de Burtă</h1>
    <h2>Meniu Interactiv</h2>
    <ul>
        <li><a href="/gastronomie">1. Tema Proiectului</a></li>
        <li><a href="/ciorba_de_burta/ingrediente">2. Ingrediente Principale</a></li>
        <li><a href="/ciorba_de_burta/descriere">3. Proveniență</a></li>
        <li><a href="/ciorba_de_burta/preparare">4. Mod de preparare</a></li>
    </ul>
    <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
    <h3>Student: Vijaica Stefan | Grupa: 444D</h3>
    '''
    return wrap_html(content)

@app.route('/gastronomie')
def tema_gastronomie():
    return wrap_html("<h1>Tema proiectului</h1><p>Acest proiect explorează arta gastronomică românească, concentrându-se pe unul dintre cele mai emblematice preparate.</p>", True)

@app.route('/ciorba_de_burta/ingrediente')
def afisare_ingrediente():
    return wrap_html(f"<h1>Ingrediente</h1><p>{ingrediente_ciorba_de_burta()}</p>", True)

@app.route('/ciorba_de_burta/descriere')
def afisare_descriere():
    return wrap_html(f"<h1>Descriere și Proveniență</h1><p>{descriere_ciorba_de_burta()}</p>", True)

@app.route('/ciorba_de_burta/preparare')
def afisare_preparare():
    return wrap_html(f"<h1>Mod de preparare</h1><p>{preparare_ciorba_de_burta()}</p>", True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
