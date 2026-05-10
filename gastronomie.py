from flask import Flask
from app.lib.biblioteca_gastronomie import provenienta_ramen, ingrediente_ramen, preparare_ramen

app = Flask(__name__)

@app.route('/')
@app.route('/gastronomie')
def tema_gastronomie():
    return '''
    <h1>Tema proiectului: Gastronomie</h1>
    <h2>Ramen</h2>
    <h3>Student: Curca Andrei-Daniel Grupa: 444D</h3>
    <ul>
        <li><a href="/ramen">0. Pagina elementului ales (Ramen)</a></li>
        <li><a href="/ramen/provenienta">1. Tara/locul de provenienta</a></li>
        <li><a href="/ramen/ingrediente">2. Ingrediente principale</a></li>
        <li><a href="/ramen/preparare">3. Modul de preparare</a></li>
    </ul>
    '''

@app.route('/ramen')
def element_ramen():
    return '''
    <h2>Element ales: Ramen</h2>
    <p>Alege una dintre informatiile de mai jos pentru a afla detalii:</p>
    <ul>
        <li><a href="/ramen/provenienta">Provenienta</a></li>
        <li><a href="/ramen/ingrediente">Ingrediente</a></li>
        <li><a href="/ramen/preparare">Modul de preparare</a></li>
    </ul>
    <br><a href="/gastronomie">⬅️ Inapoi la meniul principal</a>
    '''

@app.route('/ramen/provenienta')
def afisare_provenienta():
    rezultat = provenienta_ramen()
    return f'''
    <h2>Tara/locul de provenienta:</h2>
    <p>{rezultat}</p>
    <br><a href="/gastronomie">⬅️ Inapoi la meniul principal</a>
    '''

@app.route('/ramen/ingrediente')
def afisare_ingrediente():
    rezultat = ingrediente_ramen()
    return f'''
    <h2>Ingrediente principale:</h2>
    <p>{rezultat}</p>
    <br><a href="/gastronomie">⬅️ Inapoi la meniul principal</a>
    '''

@app.route('/ramen/preparare')
def afisare_preparare():
    rezultat = preparare_ramen()
    return f'''
    <h2>Modul de preparare:</h2>
    <p>{rezultat}</p>
    <br><a href="/gastronomie">⬅️ Inapoi la meniul principal</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

