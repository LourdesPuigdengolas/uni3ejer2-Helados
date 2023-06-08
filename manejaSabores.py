from claseSabor import Sabor
import csv

class ManejaSabores:
    __sabor: list

    def __init__(self):
        self.__sabor = []
        
    def get_sabor(self, i):
        return self.__sabor[i]
    
    def agregarSabor(self, sabor):
        self.__sabor.append(sabor) 
        
    def cargarSabores(self):
        with open("sabores.csv") as archivo:
            reader = csv.reader(archivo, delimiter=';')
            for fila in reader:
                idSabor = int(fila[0])
                nombre = fila[1]
                ingredientes = fila[2]
                sabor = Sabor(idSabor, nombre, ingredientes)
                self.agregarSabor(sabor)
                    
    
  
