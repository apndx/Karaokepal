from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name

name = "Karaokepal"

listing  = [1, 4, 2, 3, 5, 8, 11]

songs = []
songs.append(Item("First"))
songs.append(Item("Second"))
songs.append(Item("Third"))
songs.append(Item("Fourth"))

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/Karaokepal")
def content():
    return render_template("karaokepal.html", name=name, listing=listing, songs=songs)

if __name__ == "__main__":
    app.run(debug=True)
