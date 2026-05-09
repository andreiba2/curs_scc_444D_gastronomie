from flask import Flask
from app.lib.biblioteca_gastronomie import (
    get_descriere,
    get_origine,
    get_ingrediente,
    get_preparare
)

app = Flask(__name__)


@app.route('/')
def home():
    """Ruta principală care afișează pagina de start cu meniul aplicației."""
    return f"""
    <html>
        <body>
            <h1>Cheesecake</h1>
            <p>{get_descriere()}</p>
            <h3>Află mai multe detalii (Caracteristici):</h3>
            <ul>
                <li><a href="/origine">Țara/locul de proveniență</a></li>
                <li><a href="/ingrediente">Ingrediente principale</a></li>
                <li><a href="/preparare">Modul de preparare</a></li>
            </ul>
        </body>
    </html>
    """


@app.route('/origine')
def origine():
    """Ruta care afișează informații despre originea preparatului."""
    return f"""
    <html>
        <body>
            <h2>Țara/locul de proveniență</h2>
            <p>{get_origine()}</p>
            <br>
            <a href="/">⬅ Întoarce-te la Home</a>
        </body>
    </html>
    """


@app.route('/ingrediente')
def ingrediente():
    """Ruta care afișează lista de ingrediente ale preparatului."""
    return f"""
    <html>
        <body>
            <h2>Ingrediente principale</h2>
            <p>{get_ingrediente()}</p>
            <br>
            <a href="/">⬅ Întoarce-te la Home</a>
        </body>
    </html>
    """


@app.route('/preparare')
def preparare():
    """Ruta care afișează pașii pentru modul de preparare."""
    return f"""
    <html>
        <body>
            <h2>Modul de preparare</h2>
            <p>{get_preparare()}</p>
            <br>
            <a href="/">⬅ Întoarce-te la Home</a>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

