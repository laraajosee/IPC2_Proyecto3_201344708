from flask import Flask,Response, request, jsonify
from flask_cors import CORS

from gestor import Gestor
from videojuego import Videojuego
from archivo import archivo
app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

gestor = Gestor()

#Generacion de los endpoints
@app.route('/')
def home():
    return "SERVER funciona correctamente."

#Obtener juegos
@app.route('/games')
def getGames():
    return gestor.obtener_games() 

#Login
#@app.route('/login/<user>/<password>')
#def login(user=None,password=None):
 #   res = gestor.obtener_usuario(user,password)
  #  if res ==None:
   #     return '{"data":false}'
    #return '{"data":true}'

@app.route('/login/<user>/<password>')
def login(user=None,password=None):
    res = gestor.obtener_usuario(user,password)
    if res ==None:
        return '{"data":false}'
    return '{"data":true}'

#Registro de usuarios
@app.route('/registro',methods=['POST'])
def registrar_usuario():
    dato=request.json
    gestor.crear_usuario(dato['nombre'],dato['password'],dato['usuario'],dato['apellido'])
    return '{"Estado":"Usuario Creado"}'

@app.route('/stats')
def get_events():
    data = open('data.xml', 'r+', encoding='utf-8')

    return Response(response=data.read())



@app.route('/rutaArchivo', methods=["POST"])
def definirRuta():
    global archivo
    peticion=request.get_json()
    global ruta
    ruta=peticion['rutaArchivo']
    archivo.openandSave(ruta)
    if ruta!="":
        return jsonify({'data':'True'})
    else:
        return jsonify({'data':'False'})

@app.route('/imprimirEntrada', methods=["GET"])
def enviarEntrada():
    global archivo
    chi=archivo.getLineas()
    return jsonify({'entrada':chi})

@app.route('/events', methods=['POST'])
def post_events():
    print("entrando a metodo POST por la api")
    dato = request.json       
    gestor.generarArchivo(dato['nombre'])

    return Response(response=request.data.decode('utf-8'),
                    mimetype='text/plain',
                    content_type='text/plain')


#Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)
