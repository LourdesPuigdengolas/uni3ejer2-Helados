import csv

class Sabor:
    __idSabor: int
    __nombreSabor: str
    __ingredientes: str

    def __init__(self, idSabor, nombreSabor, ingredientes):
        self.__idSabor = idSabor
        self.__nombreSabor = nombreSabor
        self.__ingredientes = ingredientes

    def getidSabor(self):
        return self.__idSabor
    def getnombreSabor(self):
        return self.__nombreSabor
    def getIngredientes(self):
        return self.__ingredientes
    
    

    