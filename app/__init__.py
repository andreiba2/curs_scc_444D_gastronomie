from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        routes = [
            {"label": "Recipe", "endpoint": "/recipe"},
            {"label": "History", "endpoint": "/history"},
            {"label": "Serving Tips", "endpoint": "/serving-tips"},
        ]
        return render_template("index.html", routes=routes)

    @app.route("/recipe")
    def recipe():
        return render_template(
            "detail.html",
            title="Recipe",
            heading="Baklava Recipe",
            content="Baklava is built from layers of phyllo dough, chopped pistachios or walnuts, melted butter, and a warm syrup poured over the baked pastry.",
        )

    @app.route("/history")
    def history():
        return render_template(
            "detail.html",
            title="History",
            heading="Baklava History",
            content="Baklava has deep roots in Ottoman cuisine and became a signature dessert in Turkish bakeries, festive tables, and special celebrations.",
        )

    @app.route("/serving-tips")
    def serving_tips():
        return render_template(
            "detail.html",
            title="Serving Tips",
            heading="Serving Tips",
            content="Serve baklava slightly warm or at room temperature with Turkish tea, coffee, or a light scoop of vanilla ice cream.",
        )

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
