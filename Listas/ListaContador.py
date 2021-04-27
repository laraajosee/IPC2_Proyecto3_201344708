from Listas.NodoContador import NodoContador

class ListaContador:
    def __init__(self):
        self.inicio = None
        #self.final = None

    def insertarFinal(self, fecha, contador):
        nuevo = NodoContador(fecha, contador)
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

    def verificar(self, fecha):
        tmp = self.inicio
        verificador = False
        
        while tmp is not None:
            if(tmp.fecha == fecha):
                verificador = True
            
            tmp = tmp.siguiente
        
        return verificador     

