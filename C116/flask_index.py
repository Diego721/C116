from flask import Flask, render_template
app = Flask(__name__)

#Definir una función con diferente punto final 
'''@app.route('/index')
def first_webpage():
    #Crear una variable
    name = "Flask"
    return render_template("index.html", index_variable = name)
app.run(debug=True)'''

@app.route('/Actividad_2')
def student_webpage():
    #Crear una variable
    name = "Diego"
    return render_template("student_act.html", student_name = name)
app.run(debug=True)