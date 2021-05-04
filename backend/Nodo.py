from ListaUsuario import ListaUsuario
from ListaAfectado import ListaAfectado
from ListaError import ListaError
class Nodo:
    def __init__(self, fecha,usuario, afectado,error, estado, mensajes):
        self.fecha = fecha
        self.usuario = ListaUsuario()
        self.afectado = ListaAfectado()
        self.error = ListaError()
        self.estado = estado
        self.mensajes = mensajes
        self.siguiente = None
        self.anterior = None