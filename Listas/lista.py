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
            ListaFechas.append(tmp.fecha)
            #tmp.estado = 1
            print("Estado: "+ str(tmp.estado))
            tmp = tmp.siguiente

        for k in ListaFechas:
            temporal = k
            virgen = 0
            for n in ListaFechas:
                print("comparando:"+temporal+'con '+ n)
                if(temporal == n):
                    print("se encontro una fecha igual")
                    if(virgen == 0):
                        print("por primera vez")
                        virgen=1
                    else:
                        print("por segunda vez")

            virgen = 0
    
                
           # print(k)