from flask import Flask 
from app.lib.biblioteca_gastronomie import descriere_brasovence, ingrediente_brasovence

app = Flask(__name__)

@app.route('/gastronomie')
def tema():
	return "Tema grupei 444D este Gastronomie!"

@app.route('/brasovence')
def element():
	return "Preparatul meu: Brasovence."

@app.route('/descriere_brasovence')
def descriere():
	return descriere_brasovence()

@app.route('/ingrediente_brasovence')
def ingrediente():
	return ingrediente_brasovence()

if __name__ == '__main__':
	app.run(host='0.0.0.0' , port=5000)
