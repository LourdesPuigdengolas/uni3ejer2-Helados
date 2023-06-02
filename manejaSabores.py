from claseSabor import Sabor
import csv
class ManejaSabores:
    __sabores: list

    def __init__(self):
        self.__sabores = []
    
    def agregarSabor(self, sabor):
        self.__sabores.append(sabor) 
        
    def cargarSabores(self):
        with open('sabores.csv') as archivo:
            lector = csv.reader(archivo, delimiter=';')
            indice = 0
            for fila in lector:
                if int(fila[0]) == indice:
                    sabor = Sabor(int(fila[0]),fila[1],fila[2])
                    self.__sabores[indice-1].agregarSabores(sabor)
                else:
                    sabor= Sabor(int(fila[0]),fila[1],fila[2])
                    self.agregarSabor(sabor)
                    indice+=1
    
  
