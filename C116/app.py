#Importar el módulo Flask en el proyecto.
from flask import Flask

#Crear un objeto de la clase Flask.
app = Flask(__name__)

#La función route() de la clase Flask.
'''@app.route("/")

#‘/’ URL está vinculado con la función first_flask.
def first_flask():

    return "Este es mi primer programa en Flask"

#Ejecutamos la app en el servidor local.
app.run()'''

#Definir una función con diferente punto final 
@app.route('/flask_2')
def secound_flask():
    return "Otra prueba con flask"
app.run(debug=True)