from claseSabor import Sabor

class Helado:
    __peso: float
    __precio: float
    __sabores: list
   
    def __init__(self, peso, precio, sabor=None):
        self.__peso = peso
        self.__precio = precio
        self.sabores= []

    def agregarSabor(self, sabor):
        self.__sabores.append(sabor)
       
    def getPeso(self):
        return self.__peso
    def getPrecio(self):
        return self.__precio
    def getSaboresId(self):
        return [sabor.getidSabor() for sabor in self.__sabores]
    def getSaboresName(self):
        return [sabor.getnombreSabor() for sabor in self.__sabores]
    def getSaboresIngredientes(self):
        return [sabor.getIngredientes() for sabor in self.__sabores]
    
    
