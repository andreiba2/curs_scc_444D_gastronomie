from flask import Flask
from app.lib.biblioteca_gastronomie import text_provenienta, text_ingrediente, text_preparare

app = Flask(__name__)

style = """
<style>
    body { margin: 0; padding: 0; background: url('https://images.unsplash.com/photo-1612874742237-6526221588e3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80') no-repeat center center fixed; background-size: cover; font-family: sans-serif; }
    .overlay { background: rgba(0, 0, 0, 0.7); min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px; }
    .card { background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 20px; padding: 40px; max-width: 800px; color: white; text-align: center; }
    .student-info { font-size: 1.3em; color: #ffd700; margin-bottom: 20px; border-bottom: 2px solid rgba(255, 215, 0, 0.3); padding-bottom: 10px; font-weight: bold; }
    h1 { font-size: 3.5em; text-transform: uppercase; margin: 10px 0; }
    h2 { color: #ffd700; }
    .text { font-size: 1.1em; line-height: 1.6; text-align: justify; margin-bottom: 30px; }
    .btn { background: #ffd700; color: #000; padding: 15px 25px; text-decoration: none; border-radius: 50px; font-weight: bold; display: inline-block; margin: 10px; text-transform: uppercase; border: none; cursor: pointer; }
    .btn:hover { background: #fff; }
</style>
"""

def wrap(content):
    return f"{style}<div class='overlay'><div class='card'><div class='student-info'>Nastase Magda | 444D | Gastronomie</div>{content}</div></div>"

# RUTA 1: Tema generală
@app.route('/gastronomie')
def home():
    return wrap("<h1>Gastronomie</h1><p style='font-size:1.2em;'>Explorați universul culinar și rețetele tradiționale.</p><a href='/gastronomie/carbonara' class='btn'>Vezi Proiect: Paste Carbonara</a>")

# RUTA 2: Elementul specific (Carbonara) - ACEASTA ESTE RUTA NOUĂ CERUTĂ 
@app.route('/gastronomie/carbonara')
def element():
    return wrap("<h1>Paste Carbonara</h1><p style='font-size:1.2em; font-style:italic;'>Regina retetelor italienesti.</p><a href='/gastronomie/carbonara/provenienta' class='btn'>Provenienta</a><a href='/gastronomie/carbonara/ingrediente' class='btn'>Ingrediente</a><a href='/gastronomie/carbonara/preparare' class='btn'>Preparare</a><br><br><a href='/gastronomie' style='color:white;'>Inapoi la Tema</a>")

# RUTA 3: Informație specifică 1 (Proveniență)
@app.route('/gastronomie/carbonara/provenienta')
def prov():
    return wrap(f"<h2>Provenienta</h2><p class='text'>{text_provenienta()}</p><a href='/gastronomie/carbonara' class='btn'>Inapoi</a>")

# RUTA 4: Informație specifică 2 (Ingrediente)
@app.route('/gastronomie/carbonara/ingrediente')
def ingr():
    return wrap(f"<h2>Ingrediente</h2><p class='text'>{text_ingrediente()}</p><a href='/gastronomie/carbonara' class='btn'>Inapoi</a>")

# RUTA EXTRA (Preparare) - Păstrată pentru funcționalitate completă
@app.route('/gastronomie/carbonara/preparare')
def prep():
    return wrap(f"<h2>Preparare</h2><p class='text'>{text_preparare()}</p><a href='/gastronomie/carbonara' class='btn'>Inapoi</a>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
