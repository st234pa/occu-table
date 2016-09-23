from flask import Flask, render_template
import occupations
app = Flask(__name__)

@app.route("/")
def default():
    d = occupations.createDict()
    return render_template("occupations.html", message = occupations.select(), d=d)

@app.route("/page1")
def page1():
    return "This is page 1."

@app.route("/page2")
def page2():
    return "This is page 3."

if __name__ == "__main__":
    app.debug = True
    app.run()


