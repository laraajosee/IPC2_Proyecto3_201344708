from typing import Container
from Nodo import Nodo
#from ListaContador import ListaContador
lista =[]
ListaFechas = []
listaErrores= []
#ListaVerificar = ListaContador()
class Lista:
    def __init__(self):
        self.inicio = None
        #self.final = None

    def insertarFinal(self, fecha, usuario, afectados,error, estado,mensajes):
        nuevo = Nodo(fecha, usuario, afectados,error, estado,mensajes)
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
    
    def getNodo(self, fecha):
        tmp = self.inicio
        while tmp is not None:
            if tmp.fecha == fecha:
                return tmp
            tmp = tmp.siguiente

    def MostrarFecha(self):
        tmp = self.inicio
        
        while tmp is not None:
            print("***********************************************************************************")
            print('Fecha:',tmp.fecha + "\nCantidad De Mensajes: "+str(tmp.mensajes)+ '\nUsuario que reporta:')
            tmp.usuario.MostrarUsuario()
            print("usuarios Afectados:")
            tmp.afectado.MostrarAfectado()
            print("errores:")
            tmp.error.MostrarError()


            tmp = tmp.siguiente
    
    def comboFecha(self):
        tmp = self.inicio
        comboFecha = []
    
        
        while tmp is not None:
            
            comboFecha.append(tmp.fecha)
            

            tmp = tmp.siguiente
 
        return comboFecha

    def fecha(self,fechaa):
        tmp = self.inicio
        lista = []
        
        
        while tmp is not None:
           
            if(tmp.fecha == fechaa):
               lista = tmp.usuario.fecha()

            tmp = tmp.siguiente
        return lista

    def usuario(self,cantidad):
        tmp = self.inicio
        lista = []
        while tmp is not None:
           
            if(tmp.fecha == cantidad):
               lista = tmp.usuario.cantidad()

            tmp = tmp.siguiente
        return lista

    def errorCombo(self):
        tmp = self.inicio
        lista = []
        while tmp is not None:
            lista = tmp.error.errorCombo()
            print(lista)

            tmp = tmp.siguiente
        
        return lista
    
    def cantidadError(self,error):
        tmp = self.inicio
        lista = []
    
        
        while tmp is not None:
           
            verificador = tmp.error.cantidadError(error)
            if(verificador != None):
                lista.append(verificador)

            tmp = tmp.siguiente
        return lista

    def error(self, error):
        tmp = self.inicio
        lista = []
        
        
        while tmp is not None:
           
            verificador = tmp.error.error(error)
            if(verificador == True):
                lista.append(tmp.fecha)


            tmp = tmp.siguiente
        return lista
  

    def estadistica(self):
        tmp = self.inicio
        concatenar="<ESTADISTICAS>"
        while tmp is not None:
            #print("***********************************************************************************")
            #print('Fecha:',tmp.fecha + "\nCantidad De Mensajes: "+str(tmp.mensajes)+ '\nUsuario que reporta:')
            concatenar=concatenar+"\n\t<ESTADISTICA>"+"\n\t    <FECHA> "+tmp.fecha+" </FECHA>"+"\n\t    <CANTIDAD_MENSAJES> "+str(tmp.mensajes)+" </CANTIDAD_MENSAJES>"
            usuario = tmp.usuario.devolverString()
            concatenar=concatenar+usuario
            afectado = tmp.afectado.devolverString()
            concatenar =concatenar+afectado
            error = tmp.error.devolverString()
            concatenar=concatenar+error


            tmp = tmp.siguiente
        concatenar=concatenar+"\n</ESTADISTICAS>"
        return concatenar



    def Verificar(self, fecha):
         tmp = self.inicio
         verificar = False
        
         while tmp is not None:
           if(tmp.fecha == fecha):
               verificar = True          
       

           tmp = tmp.siguiente

         return verificar
