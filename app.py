from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    titulo="PWA"
    lista=["Alex","Luis","Pablo"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/hola")
def func():
    return "Hola ..."

@app.route("/user/<string:user>")
def func2(user):
    return "Hola: "+ user

@app.route("/numero/<int:n>")
def func3(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def func4(id,username):
    return "ID: {} nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def func5(n1,n2):
    return "La suma es: {}".format(n1+n2)

if __name__=="__main__":
    app.run(debug=True)