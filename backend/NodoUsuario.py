class NodoUsuario:
    def __init__(self,usuario, cantidadMensajes):
        self.usuario = usuario
        self.cantidadMensajes = cantidadMensajes
        self.siguiente = None
        self.anterior = None