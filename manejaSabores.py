from claseSabor import Sabor
import csv

class ManejaSabores:
    __sabores: list

    def __init__(self):
        self.__sabores = []
        
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
                    
    def obtenerNombreSaboresMasPedidos(self, n):
        sabores_mas_pedidos = sorted(self.sabores, key=lambda sabor: len(sabor.helados_vendidos), reverse=True)[:n]
        return [sabor.nombre_sabor for sabor in sabores_mas_pedidos]

  
