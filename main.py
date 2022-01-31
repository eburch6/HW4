import flask

app = flask.Flask(__name__)

favShows = ["Avatar the Last Airbender", "The Umbrella Acadamy", "The Witcher", "Disenchantment", "Stranger Things"]
showPics = ["/static/atla.jpg", "/static/umbrellaAcadamy.jpg", "/static/witcher.jpg", "/static/disenchantment.jpg", "/static/strangerThings.jpg"]

@app.route("/")

def main():
    return flask.render_template("index.html", len = len(favShows), favShows = favShows, len2 = len(showPics), showPics = showPics)

app.run(
    debug=True
)