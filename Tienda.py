from Producto import Producto

class Tienda:

    '''-----------------------------------
    #Métodos
    -----------------------------------'''

    def __init__(self):
        self.__producto1 = Producto("PAPELERIA", "Lapiz", 500, 18, 5)
        self.__producto2 = Producto("PAPELERIA", "Borrador", 300, 15, 5)
        self.__producto3 = Producto("SUPERMERCADO", "Cafe", 5.600, 20, 12)
        self.__producto4 = Producto("DROGUERIA", "Desinfectante", 3.200, 12, 10)
        self.__dineroEnCaja = 0.0

    
    def getProducto1(self):
        return self.__producto1

    def getProducto2(self):
        return self.__producto2

    def getProducto3(self):
        return self.__producto3

    def getProducto4(self):
        return self.__producto4

    def getDineroEnCaja (self):
        return self.__dineroEnCaja
