from typing import Container
from Listas.Nodo import Nodo
from Listas.ListaContador import ListaContador

ListaFechas = []
ListaVerificar = ListaContador()
class Lista:
    def __init__(self):
        self.inicio = None
        #self.final = None

    def insertarFinal(self, fecha, usuario, afectados,numeroError, error, estado,mensajes):
        nuevo = Nodo(fecha, usuario, afectados,numeroError,error, estado,mensajes)
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
            print('Fecha:',tmp.fecha, '\nUsuario que reporta:'+ tmp.usuario + '\nusuarios que reportaron: ' + str(tmp.afectado).replace(',','')
            +'\nNo. Error:'+ tmp.numeroError +  '\nError:'+ tmp.error + '\nMensajes:'+ str(tmp.mensajes))

            tmp = tmp.siguiente
    
    def ReportadoPor(self, fecha):
        concatenar = "<REPORTADO_POR>"
        contador= 0  
        tmp = self.inicio
        while tmp is not None:
            if(tmp.fecha == fecha):
                contador = contador + 1


            tmp = tmp.siguiente
        return contador


    def estadistica(self):
        tmp = self.inicio
        contador = 0
        while tmp is not None:
            buscador = 0
            
            if(len(ListaFechas) == 0):
               ListaFechas.append(tmp.fecha)
               #tmp.mensajes = +1
               tmp.estado = 1
            for k in ListaFechas:
                if(str(tmp.fecha) == str(k)):
                    buscador = 1
            if(buscador == 0):
                ListaFechas.append(tmp.fecha)
                tmp.estado = 1
    
            tmp = tmp.siguiente
       
        ordenados = sorted(ListaFechas)
     
        tmp = self.inicio
        while tmp is not None:
                contador = 0
                if(tmp.estado == 1):
                # print("---comparando: "+ tmp.fecha)
                 tmp2 = self.inicio
                 while tmp2 is not None:
                     if(tmp.fecha == tmp2.fecha):
                        #print("comparando: "+ tmp.fecha + " "+tmp2.fecha)
                        contador = contador + 1

                     tmp2 = tmp2.siguiente
                tmp.mensajes = contador
                #print("numero de mensajes en fecha: "+ tmp.fecha+" "+str(contador))
                tmp = tmp.siguiente
        estadistica = ""
        for x in ordenados:
            tmp = self.inicio
            while tmp is not None:
                reportado = Lista.ReportadoPor(tmp.fecha)

                if(x == tmp.fecha and tmp.estado == 1):
                    estadistica = estadistica+'\n  <ESTADISTICA>'+'\n    <FECHA>'+ tmp.fecha+'</FECHA>'+'\n  <CANTIDAD_MENSAJES>'+str(tmp.mensajes)+'<CANTIDAD_MENSAJES>'+'\n  </ESTADISTICA>'
                
                tmp = tmp.siguiente
        return estadistica       
