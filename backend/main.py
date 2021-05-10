from flask import Flask,Response, json, request, jsonify
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


@app.route('/registro',methods=['POST'])
def registrar_usuario():
    dato=request.json
    gestor.crear_usuario(dato['nombre'],dato['password'],dato['usuario'],dato['apellido'])
    return '{"Estado":"Usuario Creado"}'

@app.route('/stats')
def get_events():
    data = open('data.xml', 'r+', encoding='utf-8')

    return Response(response=data.read())

@app.route('/comboBox')
def comboBox():
    combo = gestor.listaCombo()
    comboError = gestor.errorCombo()
    print("lista")
    print(comboError)
    
    return jsonify(hola=combo, adios=comboError)

@app.route('/fecha',methods=["POST"])
def fecha():
    print('Entrando a fecha')
    r = request.get_json()
    print(r['data'])
    lista = gestor.fecha(r['data'])
    print('lista')
    print(lista)
    return jsonify({'data':lista})

@app.route('/error',methods=["POST"])
def error():
    print('Entrando a error')
    r = request.get_json()
    print(r['data'])
    lista = gestor.error(r['data'])
    lista2 = gestor.cantidadError(r['data'])
    print('listaaaaaaa')
    print(lista2)
    return jsonify(data=lista,data2= lista2)

@app.route('/cantidad',methods=["POST"])
def cantidad():
    r = request.get_json()
    lista = gestor.usuario(r['data'])
    print('lista')
    print(lista)
    return jsonify({'data':lista})


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

@app.route('/reiniciar',methods=['POST'])
def reiniciar():
    app.run(debug=True)
#Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)
