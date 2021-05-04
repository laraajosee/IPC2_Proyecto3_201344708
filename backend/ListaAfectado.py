from NodoAfectado import NodoAfectado

class ListaAfectado:
    def __init__(self):
        self.inicio = None
        #self.final = None

    def insertarFinal(self, correo):
        nuevo = NodoAfectado(correo)
        if self.inicio is None:
            self.inicio = nuevo
            return nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp
            return nuevo
        return None

    def getNodoAfectados(self, correo):
        tmp = self.inicio
        while tmp is not None:
            print("comparando"+ tmp.correo +'con '+ correo)
            if tmp.correo == correo:
                return tmp
            tmp = tmp.siguiente
        return None

    def MostrarAfectado(self):
        tmp = self.inicio
        
        while tmp is not None:
            print('Correo:'+ tmp.correo)

            tmp = tmp.siguiente