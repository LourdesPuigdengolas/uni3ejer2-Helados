from claseSabor import Sabor

class Helado:
    __peso: float
    __precio: float
    __sabor: list
   
    def __init__(self, peso, precio, sabor=None):
        self.__peso = peso
        self.__precio = precio
        if sabor != None:
            self.addSabor(sabor,1)

    def addSabor(self, sabor, cantidad):
        for i in range(cantidad):
            self.__sabor.append(sabor)
       
    def getPeso(self):
        return self.__peso
    def getPrecio(self):
        return self.__precio

    
