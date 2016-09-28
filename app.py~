from flask import Flask, render_template
from utils import occupations
app = Flask(__name__)

@app.route("/occupations")
def default():
    d = occupations.createDict()
    return render_template("occupations.html", message = occupations.select(), d=d)

if __name__ == "__main__":
    app.debug = True
    app.run()


