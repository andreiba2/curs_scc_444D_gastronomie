from flask import Flask
from app.biblioteca_gastronomie import provenienta_carbonara, ingrediente_carbonara, preparare_carbonara

app = Flask(__name__)

style = """
<style>
    body { 
        margin: 0; padding: 0;
        background: url('https://images.unsplash.com/photo-1612874742237-6526221588e3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80') no-repeat center center fixed; 
        background-size: cover;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }
    .overlay {
        background: rgba(0, 0, 0, 0.7);
        min-height: 100vh;
        display: flex; align-items: center; justify-content: center;
        padding: 20px;
    }
    .card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 40px;
        max-width: 750px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.8);
    }
    .student-info { 
        font-size: 1.5em; color: #ffd700; margin-bottom: 30px; 
        padding-bottom: 15px; border-bottom: 2px solid rgba(255, 215, 0, 0.3);
        font-weight: bold;
    }
    .student-info span { display: block; margin-bottom: 5px; }
    h1 { font-size: 3em; margin-bottom: 20px; text-transform: uppercase; }
    p { font-size: 1.2em; line-height: 1.6; text-align: justify; margin-bottom: 25px; }
    .btn-group { display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; margin-top: 30px; }
    .btn {
        background: #ffd700; color: #000;
        padding: 15px 30px; text-decoration: none; border-radius: 50px;
        font-weight: bold; transition: 0.3s; text-transform: uppercase;
    }
    .btn:hover { background: #fff; transform: scale(1.05); }
    .btn-alt { background: rgba(255,255,255,0.1); color: #fff; border: 1px solid #fff; }
</style>
"""

def wrap_content(content):
    return f"{style}<div class='overlay'><div class='card'><div class='student-info'><span>Student: Nastase Magda</span><span>Grupa: 444D</span></div>{content}</div></div>"

@app.route('/gastronomie')
def home():
    return wrap_content("<h1>Bucataria Italiana</h1><p>Bun venit. Astazi exploram Carbonara.</p><a href='/carbonara' class='btn'>Descopera</a>")

@app.route('/carbonara')
def details():
    return wrap_content("<h1>Paste Carbonara</h1><div class='btn-group'><a href='/provenienta' class='btn btn-alt'>Provenienta</a><a href='/ingrediente' class='btn btn-alt'>Ingrediente</a><a href='/preparare' class='btn btn-alt'>Preparare</a></div><br><br><a href='/gastronomie' class='btn'>Home</a>")

@app.route('/provenienta')
def prov():
    return wrap_content(f"<h2>Provenienta</h2><p>{provenienta_carbonara()}</p><a href='/carbonara' class='btn'>Inapoi</a>")

@app.route('/ingrediente')
def ingr():
    return wrap_content(f"<h2>Ingrediente</h2><p>{ingrediente_carbonara()}</p><a href='/carbonara' class='btn'>Inapoi</a>")

@app.route('/preparare')
def prep():
    return wrap_content(f"<h2>Preparare</h2><p>{preparare_carbonara()}</p><a href='/carbonara' class='btn'>Inapoi</a>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
