from NodoUsuario import NodoUsuario

class ListaUsuario:
    def __init__(self):
        self.inicio = None
        #self.final = None

    def insertarFinal(self, usuario, cantidadMensajes):
        nuevo = NodoUsuario(usuario, cantidadMensajes)
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

    def getNodoUsuario(self, usuario):
        tmp = self.inicio
        while tmp is not None:
            if tmp.usuario == usuario:
                return tmp
            tmp = tmp.siguiente
        return None

    def MostrarUsuario(self):
        tmp = self.inicio
        
        while tmp is not None:
            print('Correo:',tmp.usuario+ ' Cantidad de mensajes: '+ str(tmp.cantidadMensajes))

            tmp = tmp.siguiente