class Nodo:
    def __init__(self, fecha,usuario,afectados,error):
        self.fecha = fecha
        self.usuario = usuario
        self.afectado = afectados
        self.error = error
        self.siguiente = None
        self.anterior = None