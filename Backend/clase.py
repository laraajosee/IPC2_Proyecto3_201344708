from os import error
import re
from Listas.lista import Lista
from Listas.ListaAfectados import ListaAfectados
from datetime import datetime



lista = []

ListaFecha = Lista()


class backend:
   
    def prueva(self, xml):
       
        concatenar = ""
        for k in xml:
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
                concatenar = concatenar.replace("<", "")
                concatenar = concatenar.replace(">", "")
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
               # print(ConcatenarFecha)
                nodo = ListaFecha.insertarFinal(ConcatenarFecha.replace(" ",""),"","","","")  
                
            
                
            if(n == 'Reportado por:'):
                reportador = ""
                #print("REPORTADO POR:"+str(lista[contador+2]).replace('”',""))
                #ListaFecha.insertarFinal(fecha)
                #ListaFecha.MostrarFecha()
                nodo.usuario = str(lista[contador+2]).replace('”',"")
            if(n == 'Usuarios afectados:'):
      
                #print("Usuarios Afectados:"+reportador)
                lista2 = []
                UsuarioAfectado = str(lista[contador+1].replace(' ',""))
                lista2.append(UsuarioAfectado)

                ContadorAfectados = contador+2
                UsuarioAfectado = " "
                for k in range(20):
                    if(str(lista[ContadorAfectados]) != 'Error:'):
            
  
                       # print("Usuarios Afectados:"+reportador)
                        UsuarioAfectado = str(lista[ContadorAfectados]).replace(' ',"")
                        lista2.append(UsuarioAfectado)
                        ContadorAfectados = ContadorAfectados + 1
                    if(str(lista[ContadorAfectados]) == 'Error:'):
                        nodo.afectado = lista2
                        break
            if(n == 'Error:'):
                ConcanetarError = ""
                #print("Numero De Error:"+str(lista[contador+1]).replace(' ',""))
                nodo.numeroError = str(lista[contador+1]).replace('”',"")
                ContadorError = contador+2
                for k in range(20):
                    if(str(lista[ContadorError]) != 'EVENTO'):
                        ConcanetarError = ConcanetarError +" "+ str(lista[ContadorError])
                        ContadorError = ContadorError + 1
                    if(str(lista[ContadorError]) == 'EVENTO'):
                        break
               # print("Error:"+ ConcanetarError)   
                nodo.error = ConcanetarError
               
            contador = contador + 1
        ListaFecha.MostrarFecha()





         