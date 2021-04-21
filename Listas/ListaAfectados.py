from Listas.NodoAfectados import NodoAfectado

class ListaAfectados:
    def __init__(self):
        self.inicio = None
        #self.final = None

    def insertarFinal(self, CorreoAfectado):
        nuevo = NodoAfectado(CorreoAfectado)
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

    def getEstudiante(self, carnet):
        tmp = self.inicio
        while tmp is not None:
            if tmp.carnet == carnet:
                return tmp
            tmp = tmp.siguiente
        return None

    def MostrarFecha(self):
        tmp = self.inicio
        
        while tmp is not None:
            print('Correo: ',tmp.CorreoAfectado)

            tmp = tmp.siguiente