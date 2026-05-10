from flask import Flask

from app.lib.biblioteca_gastronomie import ingrediente_paella, preparare_paella

app = Flask(__name__)

@app.route('/')
def gastronomie():
    return '''
    <h1>Tema: Gastronomie</h1>
    <p>Alege un preparat:</p>
    <ul>
        <li><a href="/paella">Paella</a></li>
    </ul>
    '''

@app.route('/paella')
def paella():
    return '''
    <h1>Preparat: Paella</h1>
    <ul>
        <li><a href="/paella/ingrediente">Vezi Ingredientele</a></li>
        <li><a href="/paella/preparare">Vezi Modul de preparare</a></li>
    </ul>
    <br><a href="/"><- Înapoi la Gastronomie</a>
    '''

@app.route('/paella/ingrediente')
def ingrediente():
    info = ingrediente_paella()
    return f'''
    <h1>Ingrediente Paella</h1>
    <p>{info}</p>
    <br><a href="/paella"><- Înapoi la Paella</a>
    '''

@app.route('/paella/preparare')
def preparare():
    info = preparare_paella()
    return f'''
    <h1>Mod de preparare Paella</h1>
    <p>{info}</p>
    <br><a href="/paella"><- Înapoi la Paella</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
