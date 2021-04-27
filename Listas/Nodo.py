from Listas.ListaAfectados import ListaAfectados
class Nodo:
    def __init__(self, fecha,usuario, afectado,numeroError, error, estado, mensajes):
        self.fecha = fecha
        self.usuario = usuario
        self.afectado = []
        self.numeroError = numeroError
        self.error = error
        self.estado = estado
        self.mensajes = mensajes
        self.siguiente = None
        self.anterior = None