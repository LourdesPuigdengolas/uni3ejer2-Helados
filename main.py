from claseHelado import Helado
from claseSabor import Sabor
from manejaHelados import ManejaHelados
from manejaSabores import ManejaSabores


if __name__ == '__main__':
    sabores = ManejaSabores()
    sabores.cargarSabores()
    heladito = ManejaHelados()
    
    opcion=input('Menu\n1. Registrar helado vendido\n2. Mostrar el nombre de los 5 sabores de helado más pedidos.\n3.Estimar el total de gramos vendidos de un sabor dado.\n4.Mostrar los sabores vendidos en ese tamaño.\n5. Determinar el importe total recaudado por la Heladería, por cada tipo de helado.\n: ')
    while opcion != '0':
        if opcion == '1':
            ''' print("Opciones de sabores:")
            for sabor in maneja_sabores._ManejaSabores__sabores:
                print(f"{sabor._Sabor__idSabor}. {sabor._Sabor__nombreSabor}")
            id_sabores = input("Ingrese los IDs de los sabores separados por comas: ")
            id_sabores = [int(id_sabor) for id_sabor in id_sabores.split(",")]
            gramos = int(input("Ingrese los gramos del helado: "))
            precio = float(input("Ingrese el precio del helado: "))
            sabores = [sabor for sabor in maneja_sabores._ManejaSabores__sabores if sabor._Sabor__idSabor in id_sabores]
            helado = Helado(gramos, precio, sabores)
            maneja_helados.registrar_helado(helado)
            print("Helado registrado exitosamente.")'''
            heladito.registrarHelado()
        elif opcion == '2':
            sabores.mostrarSaboresMasPedidos()
        elif opcion == '3':
            numeroSabor = int(input('Ingrese el numero de sabor: '))
            sabores.gramosVendidosXSabor(numeroSabor)
        elif opcion == '4':
            tamaño = int(input('Ingrese el tamaño: '))
            heladito.mostrarSaboresVendidos(tamaño)
        elif opcion == '5':
            heladito.calcularTotalXTipo()

        opcion=input('Menu\n1. Registrar helado vendido\n2. Mostrar el nombre de los 5 sabores de helado más pedidos.\n3.Estimar el total de gramos vendidos de un sabor dado.\n4.Mostrar los sabores vendidos en ese tamaño.\n5. Determinar el importe total recaudado por la Heladería, por cada tipo de helado.\n: ')
            