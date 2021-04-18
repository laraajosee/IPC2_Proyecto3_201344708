from os import error
import re
from Listas.lista import Lista
from datetime import datetime


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
                concatenar = concatenar.replace("<", "")
                concatenar = concatenar.replace(">", "")
                concatenar = concatenar.replace("/", "")
                concatenar = concatenar.replace("\r", "")
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
            if(k == '-'):
                concatenar = concatenar.replace("\n", "")
                concatenar = concatenar.replace(" ", "")
                concatenar = concatenar.replace("-", "")
               # print("Guardar " + concatenar)
                lista.append(concatenar)
                concatenar = ""
     

        contador = 0
        for n in lista:  
            if(n == 'Guatemala,'):
                fecha = ""
                fecha = str(lista[contador+1]).replace(" ","")
                
                #fecha usuario afectados error
                ContadorFecha = 1
                ConcatenarFecha = ""
           
                for l in fecha:
                    ConcatenarFecha = ConcatenarFecha + l
                    if(ContadorFecha == 2):
                        ConcatenarFecha = ConcatenarFecha + "/"
                        
                    if(ContadorFecha == 4):
                        ConcatenarFecha = ConcatenarFecha + "/"
                    
                    ContadorFecha = ContadorFecha + 1
                print(ConcatenarFecha)
                ListaFecha.insertarFinal(ConcatenarFecha,"","","")
                
            if(n == 'Reportado por:'):
                reportador = ""
                print("REPORTADO POR:"+str(lista[contador+2]).replace('”',""))
                #ListaFecha.insertarFinal(fecha)
                #ListaFecha.MostrarFecha()
            if(n == 'Usuarios afectados:'):
                reportador = ""
                print("Usuarios Afectados:"+str(lista[contador+1]).replace('”',""))
                #ListaFecha.insertarFinal(fecha)
                #ListaFecha.MostrarFecha()
                ContadorAfectados = contador+2
                for k in range(20):
                    if(str(lista[ContadorAfectados]) != 'Error:'):
                        print("Usuarios Afectados:"+str(lista[ContadorAfectados]).replace('”',""))
                        ContadorAfectados = ContadorAfectados + 1
                    if(str(lista[ContadorAfectados]) == 'Error:'):
                        break
            if(n == 'Error:'):
                ConcanetarError = ""
                print("Numero De Error:"+str(lista[contador+1]).replace(' ',""))
                ContadorError = contador+2
                for k in range(20):
                    if(str(lista[ContadorError]) != 'EVENTO'):
                        ConcanetarError = ConcanetarError +" "+ str(lista[ContadorError])
                        ContadorError = ContadorError + 1
                    if(str(lista[ContadorError]) == 'EVENTO'):
                        break
                print("Error:"+ ConcanetarError)        
            contador = contador + 1

        #print(lista)
       # ListaFecha.MostrarFecha()




         