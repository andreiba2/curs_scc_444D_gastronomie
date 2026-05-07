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
        content = """
        <h3>Ingredients</h3>
        <ul>
            <li><strong>Phyllo dough:</strong> 1 pound, thawed if frozen</li>
            <li><strong>Pistachios or walnuts:</strong> 2 cups, finely chopped</li>
            <li><strong>Butter:</strong> 1 cup, melted and clarified</li>
            <li><strong>Cinnamon:</strong> 2 teaspoons</li>
            <li><strong>Cloves:</strong> ½ teaspoon, ground</li>
        </ul>
        
        <h3>For the Syrup</h3>
        <ul>
            <li><strong>Water:</strong> 2 cups</li>
            <li><strong>Sugar:</strong> 1½ cups</li>
            <li><strong>Honey:</strong> ½ cup</li>
            <li><strong>Lemon juice:</strong> 2 tablespoons</li>
            <li><strong>Cinnamon stick:</strong> 1</li>
        </ul>
        
        <h3>Instructions</h3>
        <ol>
            <li>Preheat oven to 350°F (175°C). Brush a 9x13 inch baking pan with melted butter.</li>
            <li>Mix chopped nuts with cinnamon and cloves in a bowl.</li>
            <li>Layer 8-10 sheets of phyllo dough, brushing each with melted butter.</li>
            <li>Spread half the nut mixture over the phyllo.</li>
            <li>Add 6-8 more buttered phyllo sheets, then remaining nuts.</li>
            <li>Top with 8-10 final buttered phyllo sheets.</li>
            <li>Cut into diamond or square shapes before baking.</li>
            <li>Bake for 50-60 minutes until golden brown and crispy.</li>
            <li>While baking, combine water, sugar, honey, lemon juice, and cinnamon stick. Simmer for 15 minutes.</li>
            <li>Pour hot syrup over hot baklava immediately after removing from oven.</li>
            <li>Cool completely before serving. This allows the syrup to be fully absorbed.</li>
        </ol>
        """
        return render_template(
            "detail.html",
            title="Recipe",
            heading="Authentic Baklava Recipe",
            content=content,
        )

    @app.route("/history")
    def history():
        content = """
        <p>Baklava is one of the most celebrated and beloved desserts in Middle Eastern and Mediterranean cuisine, with a rich history spanning centuries. The word "baklava" itself has uncertain origins, with some scholars tracing it to Persian or Turkic roots, reflecting the dessert's journey across the ancient Silk Road.</p>
        
        <h3>Ottoman Origins</h3>
        <p>Baklava reached its current form during the Ottoman Empire, particularly in the imperial kitchens of the Topkapi Palace in Istanbul. It became a signature dessert for celebrations, religious festivals, and royal gatherings. The meticulous layering technique and the use of premium nuts and spices reflected the sophistication of Ottoman culinary arts.</p>
        
        <h3>Spread Across Regions</h3>
        <p>As the Ottoman Empire expanded, baklava spread throughout the Balkans, Greece, the Levant, and North Africa. Each region developed its own variations, using local nuts—pistachios in Turkey and Iran, walnuts in the Levant, almonds in some Mediterranean versions. The syrup recipes also evolved, with some regions preferring honey, others adding orange blossom water or rose water.</p>
        
        <h3>Cultural Significance</h3>
        <p>Today, baklava remains a symbol of hospitality and celebration across the Middle East and Mediterranean. In Turkey, it holds such cultural importance that it's served at weddings, circumcision ceremonies, and iftar meals during Ramadan. The Gaziantep region of Turkey is particularly famous for its baklava production and is recognized by UNESCO for its culinary heritage.</p>
        """
        return render_template(
            "detail.html",
            title="History",
            heading="The Rich History of Baklava",
            content=content,
        )

    @app.route("/serving-tips")
    def serving_tips():
        content = """
        <h3>Temperature & Timing</h3>
        <p>Baklava is best enjoyed slightly warm or at room temperature. If you've made it fresh, serve it within a few hours of applying the syrup. The warmth enhances the flavors and ensures the phyllo remains crispy while the syrup is still aromatic.</p>
        
        <h3>Beverage Pairings</h3>
        <ul>
            <li><strong>Turkish Tea:</strong> The classic pairing. The bitter notes complement baklava's sweetness perfectly.</li>
            <li><strong>Turkish Coffee:</strong> Strong and thick, it balances the rich, sweet dessert.</li>
            <li><strong>Mint Tea:</strong> A refreshing alternative that aids digestion.</li>
            <li><strong>Rosewater Tea:</strong> Adds an aromatic, floral element to the experience.</li>
        </ul>
        
        <h3>Serving Suggestions</h3>
        <p>For an elegant presentation, serve baklava on a decorative plate with a small scoop of vanilla ice cream or a dollop of Greek yogurt on the side. The cool creaminess contrasts beautifully with the warm, sweet dessert. You can also garnish with a light dusting of pistachios or a sprinkle of cinnamon.</p>
        
        <h3>Storage Tips</h3>
        <p>Baklava keeps well when stored in an airtight container at room temperature for up to one week. The syrup keeps it moist and flavorful. Avoid refrigeration, as it can dry out the dessert. For longer storage, wrap individual pieces in plastic wrap and freeze for up to three months.</p>
        
        <h3>Portion Sizes</h3>
        <p>Baklava is rich and sweet—one or two pieces is typically a satisfying portion. The combination of layers, nuts, butter, and syrup makes it quite indulgent, so a little goes a long way.</p>
        """
        return render_template(
            "detail.html",
            title="Serving Tips",
            heading="How to Serve & Enjoy Baklava",
            content=content,
        )

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
