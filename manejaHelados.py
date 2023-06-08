from claseHelado import Helado
from claseSabor import Sabor
from manejaSabores import ManejaSabores

class ManejaHelados:
    __heladosVendidos: list

    def __init__(self):
        self.__heladosVendidos = []
    
    def get_listaHelados(self):
        return self.__heladosVendidos[i]
    
    def registrarHeladoVendido(self, helado):
        self.__heladosVendidos.append(helado)

    def obtenerSaboresPorTipoHelado(self, peso_helado):
        sabores = []
        for helado in self.helados_vendidos:
            if helado.peso_helado == peso_helado:
                sabores.extend(helado.sabores)
        return sabores

    def mostrarSaboresMasPedidos(self):
        importeTotalxTipo= {}
        for helado in self.helados_vendidos:
            if helado.peso_helado not in importeTotalxTipo:
                importeTotalxTipo[helado.peso_helado] = 0
            importeTotalxTipo[helado.peso_helado] += helado.precio
        return importeTotalxTipo

    def gramosVendidosXSabor(self, numeroSabor):
        gramosVendidos = 0
        idHelado = 0
        while idHelado < len(self.__helados):
            helado = self.__helados[idHelado]
            idSabor = 0
            while idSabor < len(helado._Helado__sabor):
                sabor = helado._Helado__sabor[idSabor]
                if sabor._Sabor__idSabor == numeroSabor:
                    gramos_vendidos += helado._Helado__gramos
                    break
                idSabor += 1
            idHelado += 1

        print(f"Se vendieron aproximadamente {gramosVendidos} gramos del sabor {numeroSabor}")

    def mostrarSaboresVendidos(self, tamano):
        sabor_tamano = set()
        idHelado = 0
        while idHelado < len(self.__helados):
            helado = self.__helados[idHelado]
            if helado._Helado__gramos == tamano:
                idSabor = 0
                while idSabor < len(helado._Helado__sabor):
                    sabor = helado._Helado__sabor[idSabor]
                    sabor_tamano.add(sabor._Sabor__idSabor)

                    idSabor += 1
            idHelado += 1

        print(f"Sabores vendidos en helados de {tamano} gramos:")
        for sabor in sabor_tamano:
            print(f"ID del sabor: {sabor}")

    def calcularTotalXTipo(self):
        importe_total = 0
        idHelado = 0
        while idHelado < len(self.__helados):
            helado = self.__helados[idHelado]
            importe_total += helado._Helado__precio
            idHelado += 1

        print(f"El importe total recaudado es de ${importe_total:.2f} pesos")