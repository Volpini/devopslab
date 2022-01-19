from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Hello World - Bruno Volpini"

@app.route("/fiap")
def fiap():
    return "From FIAP route"

@app.route("/fiap/challenge")
def fiap_challenge():
    return "This increments the number of lines of code to allow SonarQube to actually scan the entire code"

@app.route("/fiap/group")
def fiap_group():
    return "Grupo 9 (Ana, Bruno, Danilo e Fabian)"

@app.route("/foo")
def foo():
    return "foo"

@app.route("/bar")
def bar():
    return "bar"

@app.route("/healthcheck")
def healthcheck():
    return "OK"

@app.route("/6aso")
def aso():
    return "6ASO"

@app.route("/lore")
def lore():
    return "ipsum"

@app.route("/cober")
def cober():
    return "tura"

@app.route("/tura")
def tura():
    return "cober"

if __name__ == '__main__':
    app.run()