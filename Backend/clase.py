import re
from Listas.lista import Lista

lista = []
ListaFecha = Lista()


class backend:
   
    def prueva(self, xml):
       
        concatenar = ""
        for k in xml:
            #res = [ord(ele) for sub in k for ele in sub]
            #print(res)
            concatenar = concatenar + k
            if(k == '\n'):
                concatenar = concatenar.replace("\n", "")
                #print("Guardar " + concatenar)
                lista.append(concatenar)
                concatenar = ""
            if(k == ','):
                concatenar = concatenar.replace("\n", "")
                #print("Guardar " + concatenar)
                lista.append(concatenar)
                concatenar = ""
            if(k == ':'):
                concatenar = concatenar.replace("\n", "")
               # print("Guardar " + concatenar)
                lista.append(concatenar)
                concatenar = ""
            if(k == '”'):
                concatenar = concatenar.replace("\n", "")
               # print("Guardar " + concatenar)
                lista.append(concatenar)
                concatenar = ""

        contador = 0
        for n in lista:  
            if(n == 'Guatemala,'):
                fecha = ""
                fecha = str(lista[contador+1]).replace(" ","")
                print("esta es la fecha:"+fecha)
                ListaFecha.insertarFinal(fecha)
                ListaFecha.MostrarFecha()
            if(n == 'Reportado por:'):
                reportador = ""
                print("REPORTADO POR:"+str(lista[contador+2]).replace('”',""))
                #ListaFecha.insertarFinal(fecha)
                #ListaFecha.MostrarFecha()

            print(n)
            contador = contador +1
            
      
        
        #contador = 0
       # print(re.split('\r|\n,', str(xml)))

        #x = str(xml).split(" ")
        #print("hola: :"+ str(x))

       # res = [ord(ele) for sub in xml for ele in sub]
        #print(res)




         