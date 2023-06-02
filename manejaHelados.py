from claseHelado import Helado
from claseSabor import Sabor
from manejaSabores import ManejaSabores

class ManejaHelados:
    __listaHelados: list

    def __init__(self):
        self.__listaHelados = []
    
    def get_listaHelados(self):
        return self.__listaHelados[i]
    
    def registrarHelado(self, helado):
        self.__listaHelados.append(helado)

    def registrarHelado(self):
        venta=int(input(print('Ingrese numero de venta')))
        while venta != '0':
            peso = float(input('Ingrese el peso del helado: '))
            precio = float(input('Ingrese el precio del helado: '))
            sabores = int(input('Ingrese el id del sabor 1: '))
            unHelado=Helado(peso, precio,sabores)
            self.registrarHelado.append(unHelado) 
            venta=int(input(print('Helado registrado con exito!, si desea ingresar otra venta ingrese numero de venta, de lo contrario ingrese 0')))
    
    def mostrarSaboresMasPedidos(self):
        cantSabores= Counter()
        idHelado = 0
        while idHelado < len(self.__helados):
            helado = self.__helados[idHelado]
            idSabor = 0
            while idSabor < len(helado._Helado__sabores):
                sabor = helado._Helado__sabores[idSabor]
                contadorSabores[sabor._Sabor__idSabor] += 1
                idSabor += 1
            idHelado += 1

        masPedidos = contadorSabores.most_common(5)
        print("Los 5 sabores más pedidos son:")
        for sabor, cantidad in masPedidos:
            print(f"ID del sabor: {sabor}, cantidad de pedidos: {cantidad}")

    def gramosVendidosXSabor(self, numeroSabor):
        gramosVendidos = 0
        idHelado = 0
        while idHelado < len(self.__helados):
            helado = self.__helados[idHelado]
            idSabor = 0
            while idSabor < len(helado._Helado__sabores):
                sabor = helado._Helado__sabores[idSabor]
                if sabor._Sabor__idSabor == numeroSabor:
                    gramos_vendidos += helado._Helado__gramos
                    break
                idSabor += 1
            idHelado += 1

        print(f"Se vendieron aproximadamente {gramosVendidos} gramos del sabor {numeroSabor}")

    def mostrarSaboresVendidos(self, tamano):
        sabores_tamano = set()
        idHelado = 0
        while idHelado < len(self.__helados):
            helado = self.__helados[idHelado]
            if helado._Helado__gramos == tamano:
                idSabor = 0
                while idSabor < len(helado._Helado__sabores):
                    sabor = helado._Helado__sabores[idSabor]
                    sabores_tamano.add(sabor._Sabor__idSabor)
                    idSabor += 1
            idHelado += 1

        print(f"Sabores vendidos en helados de {tamano} gramos:")
        for sabor in sabores_tamano:
            print(f"ID del sabor: {sabor}")

    def calcularTotalXTipo(self):
        importe_total = 0
        idHelado = 0
        while idHelado < len(self.__helados):
            helado = self.__helados[idHelado]
            importe_total += helado._Helado__precio
            idHelado += 1

        print(f"El importe total recaudado es de ${importe_total:.2f} pesos")