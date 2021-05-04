from ListaUsuario import ListaUsuario
from ListaAfectado import ListaAfectado
class Nodo:
    def __init__(self, fecha,usuario, afectado,numeroError, error, estado, mensajes):
        self.fecha = fecha
        self.usuario = ListaUsuario()
        self.afectado = ListaAfectado()
        self.numeroError = numeroError
        self.error = error
        self.estado = estado
        self.mensajes = mensajes
        self.siguiente = None
        self.anterior = None