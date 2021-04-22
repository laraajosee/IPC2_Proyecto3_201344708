from Listas.Nodo import Nodo

ListaFechas = []
class Lista:
    def __init__(self):
        self.inicio = None
        #self.final = None

    def insertarFinal(self, fecha, usuario, afectados,numeroError, error, estado):
        nuevo = Nodo(fecha, usuario, afectados,numeroError,error, estado)
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
            +'\nNo. Error:'+ tmp.numeroError +  '\nError:'+ tmp.error)

            tmp = tmp.siguiente

    def estadistica(self):
        tmp = self.inicio
        contador = 0
        while tmp is not None:
            buscador = 0
            #print("el tamano de la lista es de: "+ str(len(ListaFechas)))
            if(len(ListaFechas) == 0):
               ListaFechas.append(tmp.fecha)
               tmp.estado = 1
            for k in ListaFechas:
               # print("comparando"+ tmp.fecha+"con"+ k)
                if(str(tmp.fecha) == str(k)):
                    buscador = 1

            #print("cambio buscador a "+ str(buscador))    

            if(buscador == 0):
                ListaFechas.append(tmp.fecha)
                tmp.estado = 1
    
            tmp = tmp.siguiente
        print(ListaFechas)  

        tmp = self.inicio
        while tmp is not None:
            print('Fecha:'+ tmp.fecha  +' \nestado: '+ str(tmp.estado))
            tmp = tmp.siguiente

      