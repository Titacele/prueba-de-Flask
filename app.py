from flask import Flask
#importamos el renderizador, es para navegar entre paginas
from flask import render_template

# punto de entrada a la aplicación
app = Flask(__name__)

#cuando se usa cierta ruta, se ejecuta cierta función
#@app.route("route")
#def func():
@app.route("/")
def index():
    return render_template('empleados/index.html')



if __name__=='__main__':
    app.run(debug=True)
