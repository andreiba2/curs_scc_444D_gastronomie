from flask import Flask
from app.lib.biblioteca_gastronomie import culoare_carbonara, descriere_carbonara, alternative_carbonara

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
        font-size: 1.5em; 
        color: #ffd700; 
        margin-bottom: 30px; 
        padding-bottom: 15px;
        border-bottom: 2px solid rgba(255, 215, 0, 0.3);
        font-weight: bold;
    }
    .student-info span { display: block; margin-bottom: 5px; }
    h1 { font-size: 3em; margin-bottom: 20px; text-transform: uppercase; color: #fff; }
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
    return f"{style}<div class='overlay'><div class='card'><div class='student-info'><span>Student: Nastase Magda</span><span>Grupa: 444D</span><span>Tema: Gastronomie</span></div>{content}</div></div>"

@app.route('/gastronomie')
def tema():
    return wrap_content("<h1>Bucataria Italiana</h1><p>Bun venit in universul gustului autentic. Astazi exploram regele pastelor romane, un simbol al traditiei si simplitatii perfecte.</p><a href='/carbonara' class='btn'>Descopera Carbonara</a>")

@app.route('/carbonara')
def element():
    return wrap_content("<h1>Paste Carbonara</h1><p>O reteta simpla ca ingrediente, dar care necesita precizie absoluta.</p><div class='btn-group'><a href='/culoare_carbonara' class='btn btn-alt'>Aspect</a><a href='/descriere_carbonara' class='btn btn-alt'>Reteta</a><a href='/alternative' class='btn btn-alt'>Alternative</a></div><br><br><a href='/gastronomie' class='btn'>Inapoi la Home</a>")

@app.route('/culoare_carbonara')
def culoare():
    return wrap_content(f"<h2>Analiza Vizuala</h2><p>{culoare_carbonara()}</p><a href='/carbonara' class='btn'>Inapoi</a>")

@app.route('/descriere_carbonara')
def descriere():
    return wrap_content(f"<h2>Tehnica si Reteta</h2><p>{descriere_carbonara()}</p><a href='/carbonara' class='btn'>Inapoi</a>")

@app.route('/alternative')
def alternative():
    return wrap_content(f"<h2>Variatiuni Moderne</h2><p>{alternative_carbonara()}</p><a href='/carbonara' class='btn'>Inapoi</a>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
