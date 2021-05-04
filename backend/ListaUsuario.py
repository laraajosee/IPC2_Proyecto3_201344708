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

    def devolverString(self):
        tmp = self.inicio
        #concatenar=""
        concatenar= "\n\t<REPORTADO_POR>"
        while tmp is not None:
            #print('Correo:',tmp.usuario+ ' Cantidad de mensajes: '+ str(tmp.cantidadMensajes))
            concatenar=concatenar+"\n\t    <EMAIL> "+tmp.usuario+" </EMAIL>"+"\n\t    <CANTIDAD_MENSAJES> "+str(tmp.cantidadMensajes)+" <CANTIDAD_MENSAJES>"

            tmp = tmp.siguiente
        concatenar = concatenar+ "\n\t</REPORTADO_POR>"
        return concatenar

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