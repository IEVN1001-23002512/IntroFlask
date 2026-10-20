from flask import Flask, render_template, request
import math

app=Flask(__name__)

@app.route('/')
def index():
    titulo="PWA"
    lista=["Alex","Luis","Pablo"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/operasBas", methods=["GET", "POST"])
def operasBas():
    n1=0
    n2=0
    res=0
    operacion=''
    if request.method=='POST':
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        if request.form.get('operacion')== 'sumar':
            res=float(n1)+float(n2)
        if request.form.get('operacion')== 'restar':
            res=float(n1)-float(n2)
        if request.form.get('operacion')== 'multiplicar':
            res=float(n1)*float(n2)
    return render_template("operasBas.html", n1=n1, n2=n2, res=res)

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    x1=0
    x2=0
    y1=0
    y2=0
    dis=0
    if request.method=='POST':
        x1=request.form.get('x1')
        x2=request.form.get('x2')
        y1=request.form.get('y1')
        y2=request.form.get('y2')
        dis=math.sqrt(math.pow(float(x2)-float(x1),2) + math.pow(float(y2)-float(y1),2))
    return render_template("distancia.html", dis=dis)

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