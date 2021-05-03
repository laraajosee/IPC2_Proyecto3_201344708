class archivo:
    def openandSaveFile(self,ruta):
        try: 
            self.ruta = ruta
            self.lineas.clear()
            archivo=open(self.ruta,'r')
            for linea in archivo:
                linea=linea.strip()
                self.lineas.append(linea)
        except:
            print("Error")