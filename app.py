from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Hello World - Bruno Volpini"

@app.route("/fiap")
def pagina_inicial():
    return "From FIAP route"

@app.route("/fiap/challenge")
def pagina_inicial():
    return "This increments the number of lines of code to allow SonarQube to actually scan the entire code"

@app.route("/fiap/group")
def pagina_inicial():
    return "Grupo 9 (Ana, Bruno, Danilo e Fabian)"

@app.route("/foo")
def pagina_inicial():
    return "foo"

@app.route("/bar")
def pagina_inicial():
    return "bar"

@app.route("/healthcheck")
def pagina_inicial():
    return "OK"

@app.route("/6aso")
def pagina_inicial():
    return "6ASO"

@app.route("/lore")
def pagina_inicial():
    return "ipsum"

if __name__ == '__main__':
    app.run()