from flask import Flask
from app.lib.biblioteca_gastronomie import ingrediente_ciorba_de_burta, descriere_ciorba_de_burta, preparare_ciorba_de_burta

app = Flask(__name__)

@app.route('/')
def meniu_principal():
    return '''
    <h1>Proiect Gastronomie: Ciorba de Burta</h1>
    <h2>Meniu Interactiv</h2>
    <h3>Student: Vijaica Stefan: 444D</h3>
    <ul>
        <li><a href="/gastronomie">1. Tema Proiectului</a></li>
        <li><a href="/ciorba_de_burta/ingrediente">2. Ingrediente Principale</a></li>
        <li><a href="/ciorba_de_burta/descriere">3. Tara/Locul de provenienta</a></li>
        <li><a href="/ciorba_de_burta/preparare">4. Modul de preparare</a></li>
    </ul>
    '''

@app.route('/gastronomie')
def tema_gastronomie():
    return "<h1>Tema proiectului este: Gastronomie</h1><br><a href='/'>Inapoi la meniu</a>"

@app.route('/ciorba_de_burta/ingrediente')
def afisare_ingrediente():
    return f"<h1>Ingrediente:</h1><p>{ingrediente_ciorba_de_burta()}</p><br><a href='/'>Inapoi</a>"

@app.route('/ciorba_de_burta/descriere')
def afisare_descriere():
    return f"<h1>Provenienta/Descriere:</h1><p>{descriere_ciorba_de_burta()}</p><br><a href='/'>Inapoi</a>"

@app.route('/ciorba_de_burta/preparare')
def afisare_preparare():
    return f"<h1>Mod de preparare:</h1><p>{preparare_ciorba_de_burta()}</p><br><a href='/'>Inapoi</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
