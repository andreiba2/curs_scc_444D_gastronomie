from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    food = {
        "name": "Tajin",
        "description": "Tajin este un preparat traditional marocan gatit lent cu carne, legume si condimente aromate.",
        "image": "https://images.unsplash.com/photo-1541518763669-27fef04b14ea"
    }

    return render_template("index.html", food=food)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
