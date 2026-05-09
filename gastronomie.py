from flask import Flask
from app.lib.biblioteca_gastronomie import (
    provenienta_chilli_con_carne,
    ingrediente_chilli_con_carne,
    preparare_chilli_con_carne
)

app = Flask(__name__)

@app.route('/')
@app.route('/gastronomie')
def tema_gastronomie():
    return '''
    <h1>Tema proiectului: Gastronomie</h1>
    <h2>Chilli con carne</h2>
    <h3>Student: Antoci George-Cosmin</h3>
    <h3>Grupa: 444D</h3>
    <ul>
        <li><a href="/chilli_con_carne/provenienta">1. Tara/locul de provenienta</a></li>
        <li><a href="/chilli_con_carne/ingrediente">2. Ingrediente principale</a></li>
        <li><a href="/chilli_con_carne/preparare">3. Modul de preparare</a></li>
    </ul>
    '''

@app.route('/chilli_con_carne')
def chilli_con_carne():
    return '''
    <h2>Element ales: Chilli con carne</h2>
    <br><a href="/gastronomie">⬅️ Inapoi la meniul principal</a>
    '''

@app.route('/chilli_con_carne/provenienta')
def afisare_provenienta():
    rezultat = provenienta_chilli_con_carne()
    return f'''
    <h2>Tara/locul de provenienta:</h2>
    <p>{rezultat}</p>
    <br><a href="/gastronomie">⬅️ Inapoi la meniul principal</a>
    '''

@app.route('/chilli_con_carne/ingrediente')
def afisare_ingrediente():
    rezultat = ingrediente_chilli_con_carne()
    return f'''
    <h2>Ingrediente principale:</h2>
    <p>{rezultat}</p>
    <br><a href="/gastronomie">⬅️ Inapoi la meniul principal</a>
    '''

@app.route('/chilli_con_carne/preparare')
def afisare_preparare():
    rezultat = preparare_chilli_con_carne()
    return f'''
    <h2>Modul de preparare:</h2>
    <p>{rezultat}</p>
    <br><a href="/gastronomie">⬅️ Inapoi la meniul principal</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
