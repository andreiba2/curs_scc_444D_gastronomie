from flask import Flask
from app.lib.biblioteca_gastronomie import culoare_carbonara, descriere_carbonara

app = Flask(__name__)

# Cerinta: Nume, Prenume, Grupa si Tema
info = "<p><b>Student:</b> Nastase Magda</p><p><b>Grupa:</b> 444D</p><p><b>Tema:</b> Gastronomie</p>"

@app.route('/gastronomie')
def tema():
    return f"{info} <h2>Pagina Temei</h2> <a href='/carbonara'>Vezi Preparatul</a>"

@app.route('/carbonara')
def element():
    return f"{info} <h2>Element ales: Paste Carbonara</h2> <a href='/culoare_carbonara'>Vezi Culoare</a> | <a href='/descriere_carbonara'>Vezi Descriere</a> | <a href='/gastronomie'>Inapoi</a>"

@app.route('/culoare_carbonara')
def culoare():
    return f"{info} <h3>Culoare:</h3> {culoare_carbonara()} <br><br> <a href='/carbonara'>Inapoi</a>"

@app.route('/descriere_carbonara')
def descriere():
    return f"{info} <h3>Descriere:</h3> {descriere_carbonara()} <br><br> <a href='/carbonara'>Inapoi</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
