from flask import Flask
from app.lib.biblioteca_gastronomie import provenienta_gulas, ingrediente_gulas, preparare_gulas

app = Flask(__name__)

BUTTONS_HTML = (
    "<div style='margin-top:1rem;'>"
    "<a href='/gulas/provenienta_gulas' style='display:inline-block;margin:0.4rem;padding:0.8rem 1.2rem;background:#007bff;color:#fff;text-decoration:none;border-radius:0.3rem;'>Proveniență</a>"
    "<a href='/gulas/ingrediente_gulas' style='display:inline-block;margin:0.4rem;padding:0.8rem 1.2rem;background:#007bff;color:#fff;text-decoration:none;border-radius:0.3rem;'>Ingrediente</a>"
    "<a href='/gulas/preparare_gulas' style='display:inline-block;margin:0.4rem;padding:0.8rem 1.2rem;background:#007bff;color:#fff;text-decoration:none;border-radius:0.3rem;'>Preparare</a>"
    "</div>"
)
BACK_BUTTON_HTML = (
    "<div style='margin-top:1rem;'>"
    "<a href='javascript:history.back()' style='display:inline-block;margin:0.4rem;padding:0.8rem 1.2rem;background:#6c757d;color:#fff;text-decoration:none;border-radius:0.3rem;'>Înapoi</a>"
    "</div>"
)

@app.route('/')
@app.route('/gastronomie')
def gastronomie():
    return ("<h1>Tema: Gastronomie - Gulaș</h1>"
            f"{BUTTONS_HTML}")

@app.route('/gulas')
def gulas():
    return ("<h1>Gulaș</h1><p>Un preparat iconic din bucătăria central-europeană.</p>"
            f"{BACK_BUTTON_HTML}")

@app.route('/gulas/provenienta_gulas')
def get_provenienta_gulas():
    return (f"<p>{provenienta_gulas()}</p>"
            f"{BACK_BUTTON_HTML}")

@app.route('/gulas/ingrediente_gulas')
def get_ingrediente_gulas():
    return (f"<p>{ingrediente_gulas()}</p>"
            f"{BACK_BUTTON_HTML}")

@app.route('/gulas/preparare_gulas')
def get_preparare_gulas():
    return (f"<p>{preparare_gulas()}</p>"
            f"{BACK_BUTTON_HTML}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
