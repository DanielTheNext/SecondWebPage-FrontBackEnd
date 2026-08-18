from flask import Flask
import random

app = Flask(__name__)

facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos", "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna", "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo", "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo", "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos", "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos", "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]

@app.route("/")
def hello_world():
    return f'<p>Home page</p><a href="/random_fact">¡Ver un dato aleatorio!</a><p>Descifra esto con un traductor binario y ve el link secreto: 01000101 01110011 01110100 01100101 00100000 01100101 01110011 00100000 01100101 01101100 00100000 01101100 01101001 01101110 01101011 00100000 00111010 00100000 00101111 01110011 01100101 01100011 01110010 01100101 01110100 01011111 00110000 00110100 00110100 00110010 00110011 00110100 00110100 00110101 00111001 00110010 00110011 00110100 00111000 01100110 01001011 00111000 00110001 00110010 00110011 01110000 00110011 00110011 01110010 01011001 01110100 01001011 01010101 00110111 00110010 00110011</p'

@app.route("/secret_0442344592348fK8123p33rYtKU723")
def pato():
    return f'<img src="/static/fantasmita.png" alt="Image 1">'

@app.route("/random_fact")
def data():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)