class NodoContador:
    def __init__(self,fecha, contador):
        self.fecha = fecha
        self.contador = contador
        self.siguiente = None
        self.anterior = None