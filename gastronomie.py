from flask import Flask
from app.lib.biblioteca_gastronomie import ingrediente_lasagna, preparare_lasagna

app = Flask(__name__)

@app.route('/')
def gastronomie():
    return '''
    <h1>Tema: Gastronomie</h1>
    <p>Alege un preparat:</p>
    <ul>
        <li><a href="/lasagna">Lasagna</a></li>
    </ul>
    '''

@app.route('/lasagna')
def lasagna():
    return '''
    <h1>Preparat: Lasagna</h1>
    <ul>
        <li><a href="/lasagna/ingrediente">Vezi Ingredientele</a></li>
        <li><a href="/lasagna/preparare">Vezi Modul de preparare</a></li>
    </ul>
    <br><a href="/"><- Înapoi la Gastronomie</a>
    '''

@app.route('/lasagna/ingrediente')
def ingrediente(): 
    info = ingrediente_lasagna()
    return f'''
    <h1>Ingrediente Lasagna</h1>
    <p>{info}</p>
    <br><a href="/lasagna"><- Înapoi la Lasagna</a>
    '''

@app.route('/lasagna/preparare')
def preparare():
    info = preparare_lasagna()
    return f'''
    <h1>Mod de preparare Lasagna</h1>
    <p>{info}</p>
    <br><a href="/lasagna"><- Înapoi la Lasagna</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
