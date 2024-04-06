from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quem-somos")
def about():
    return render_template("quemsomos.html")

@app.route("/contato")
def contact():
    return render_template("contato.html")
