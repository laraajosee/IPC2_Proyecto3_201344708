from NodoError import NodoError

lista = []
class ListaError:
    def __init__(self):
        self.inicio = None
        #self.final = None

    def insertarFinal(self, error, cantidadMensajes):
        nuevo = NodoError(error, cantidadMensajes)
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

    def getNodoError(self, usuario):
        tmp = self.inicio
        while tmp is not None:
            if tmp.error == usuario:
                return tmp
            tmp = tmp.siguiente
        return None

    def MostrarError(self):
        tmp = self.inicio
        
        while tmp is not None:
            print('Error:',tmp.error+ ' Cantidad de mensajes: '+ str(tmp.cantidadMensajes))

            tmp = tmp.siguiente
    
    def cantidadError(self,error):
        tmp = self.inicio
        print("entro en cantidad error:" +error)
        while tmp is not None:
            print('comparanto '+tmp.error+"con " +error)
            if(tmp.error == error):
                print("entro al if")
                errorRegreso = tmp.cantidadMensajes
                return errorRegreso 


            tmp = tmp.siguiente



    
    def error(self,error):
        tmp = self.inicio
        verificar = False
        
        while tmp is not None:
            if(tmp.error == error):
                verificar = True

            tmp = tmp.siguiente
        return verificar


    def errorCombo(self):
        tmp = self.inicio
        verificador = False
        
        while tmp is not None:
            for n in lista:
                if(tmp.error == n):
                 verificador = True
                
            if( verificador== False):
                 lista.append(tmp.error)
                
           
            tmp = tmp.siguiente

        return lista

    def devolverString(self):
        tmp = self.inicio
        concatenar ="\n\t<ERRORES>"
        while tmp is not None:
            #print('Error:',tmp.error+ ' Cantidad de mensajes: '+ str(tmp.cantidadMensajes))
            concatenar=concatenar+"\n\t    <ERROR> "+tmp.error+"</ERROR>"+"\n\t    <CANTIDAD_MENSAJES> "+str(tmp.cantidadMensajes)+" <CANTIDAD_MENSAJES>"
            tmp = tmp.siguiente
        
        concatenar=concatenar+"\n\t</ERRORES>"
        return concatenar