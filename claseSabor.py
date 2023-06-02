
class Sabor:
    __idSabor: int
    __nombre: str
    __ingredientes: str

    def __init__(self, idSabor, nombre, ingredientes):
        self.__idSabor = idSabor
        self.__nombre = nombre
        self.__ingredientes = ingredientes

    def getidSabor(self):
        return self.__idSabor
    def getNombre(self):
        return self.__nombre
    def getIngredientes(self):
        return self.__ingredientes
    
    

    