class NodoError:
    def __init__(self,error, cantidadMensajes):
        self.error = error
        self.cantidadMensajes = cantidadMensajes
        self.siguiente = None
        self.anterior = None