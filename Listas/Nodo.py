from Listas.ListaAfectados import ListaAfectados
class Nodo:
    def __init__(self, fecha,usuario, afectado,numeroError, error):
        self.fecha = fecha
        self.usuario = usuario
        self.afectado = []
        self.numeroError = numeroError
        self.error = error
        self.siguiente = None
        self.anterior = None