from flask import Flask
from app.lib.lib_gastronomie import descriere, ingrediente, preparare, provenienta

app = Flask(__name__)

@app.route('/')
def tema_gastronomie():
    return '''
        <h1>Tema proiectului: Gastronomie</h1>
        <h2><a>Lava Cake</a></h2>
    '''

@app.route('/lava-cake')
def details():
    return f'''
        <p>{descriere()}</p>

        <ul>
            <li><a href="/lava-cake/provenienta">Provenienta</a></li>
            <li><a href="/lava-cake/ingrediente">Ingrediente</a></li>
            <li><a href="/lava-cake/preparare">Mod de preparare</a></li>
        </ul>
    '''
@app.route('/lava-cake/provenienta')
def afisare_provenienta():
    rezultat = provenienta()
    return f'{rezultat}'

@app.route('/lava-cake/ingrediente')
def afisare_ingrediente():
    rezultat = ingrediente()
    return f'{rezultat}'

@app.route('/lava-cake/preparare')
def afisare_preparare():
    rezultat = preparare()
    return f'{rezultat}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)