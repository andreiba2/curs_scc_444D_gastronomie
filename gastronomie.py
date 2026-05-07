from flask import Flask

app = Flask(__name__)

style = """
<style>
    body { margin: 0; padding: 0; background: url('https://images.unsplash.com/photo-1612874742237-6526221588e3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80') no-repeat center center fixed; background-size: cover; font-family: sans-serif; }
    .overlay { background: rgba(0, 0, 0, 0.7); min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px; }
    .card { background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 20px; padding: 40px; max-width: 800px; color: white; text-align: center; }
    .student-info { font-size: 1.3em; color: #ffd700; margin-bottom: 20px; border-bottom: 2px solid rgba(255, 215, 0, 0.3); padding-bottom: 10px; font-weight: bold; }
    h1 { font-size: 3.5em; text-transform: uppercase; margin: 10px 0; }
    .intro { font-size: 1.2em; font-style: italic; margin-bottom: 30px; }
    .text { font-size: 1.1em; line-height: 1.6; text-align: justify; margin-bottom: 30px; }
    .btn { background: #ffd700; color: #000; padding: 15px 25px; text-decoration: none; border-radius: 50px; font-weight: bold; display: inline-block; margin: 10px; text-transform: uppercase; }
</style>
"""

def wrap(content):
    return f"{style}<div class='overlay'><div class='card'><div class='student-info'>Nastase Magda | 444D | Gastronomie</div>{content}</div></div>"

@app.route('/gastronomie')
def home():
    return wrap("<h1>Paste Carbonara</h1><p class='intro'>Regina retetelor italienesti, un simbol al traditiei si simplitatii perfecte.</p><a href='/provenienta' class='btn'>Provenienta</a><a href='/ingrediente' class='btn'>Ingrediente</a><a href='/preparare' class='btn'>Preparare</a>")

@app.route('/provenienta')
def prov():
    msg = "Pasta alla Carbonara provine din regiunea Lazio, Italia, avand centrul in Roma. Numele sugereaza o legatura cu 'carbonari', muncitorii care pregateau acest fel de mancare satios in munti. O alta legenda spune ca reteta a aparut in 1944, cand soldatii americani au adus ratii de oua si bacon, pe care bucatarii romani le-au combinat cu paste. Indiferent de origine, Carbonara a devenit rapid un simbol global al simplitatii italiene. Astazi, este protejata de puristi, fiind considerata o mostenire culturala ce refuza smantana, pastrand gustul autentic al Romei de alta data in fiecare farfurie servita cu pasiune."
    return wrap(f"<h2>Provenienta</h2><p class='text'>{msg}</p><a href='/gastronomie' class='btn'>Inapoi</a>")

@app.route('/ingrediente')
def ingr():
    msg = "Reteta autentica se bazeaza pe cinci ingrediente sacre. Guanciale, gusa de porc maturata, ofera grasimea nobila si aroma intensa. Pecorino Romano, branza de oaie sarata, confera caracterul picant. Galbenusurile proaspete creeaza o emulsie aurie, fara a folosi smantana. Piperul negru macinat mare aduce contrastul necesar, amintind de praful de carbune al vechilor muncitori. In final, pastele din grau dur, spaghetti sau rigatoni, absorb perfect sosul catifelat. Calitatea acestor elemente este cruciala; fara ele, Carbonara isi pierde sufletul. Traditia romana interzice usturoiul sau ceapa, punand accent pe aromele pure si echilibrul perfect intre grasime, sare si textura matasoasa a oului."
    return wrap(f"<h2>Ingrediente</h2><p class='text'>{msg}</p><a href='/gastronomie' class='btn'>Inapoi</a>")

@app.route('/preparare')
def prep():
    msg = "Prepararea necesita sincronizare perfecta. Se incepe prin rumenirea lenta a bucatelelor de guanciale pana devin crocante. Separat, se amesteca galbenusurile cu Pecorino razuit fin si piper negru pana se obtine o pasta densa. Pastele se fierb al dente, pastrand putina apa de fierbere. Momentul cheie este emulsia: pastele fierbinti se pun peste guanciale, se ia tigaia de pe foc si se adauga amestecul de ou. Caldura reziduala gateste oul fara a-l transforma in omleta, creand un sos cremos cu ajutorul apei de paste. Rezultatul trebuie sa fie stralucitor si dens, imbracand fiecare pasta intr-o explozie de arome traditionale romane savurate instantaneu."
    return wrap(f"<h2>Preparare</h2><p class='text'>{msg}</p><a href='/gastronomie' class='btn'>Inapoi</a>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
