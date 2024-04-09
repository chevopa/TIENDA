class Producto:
    
    '''---------------------------------------
    #Metodos
    ----------------------------------------'''
    def __init__(self, pTipo, pNombre, pValorUnitario, pCantidadBodega, pCantidadMinima):
        self.__tipo = pTipo
        self.__nombre = pNombre
        self.__valorUnitario = pValorUnitario
        self.__cantidadBodega = pCantidadBodega
        self.__cantidadMinima = pCantidadMinima
        self.__cantidadUnidadesVendidas = 0

    def getNombre( self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__valorUnitario

    def getCantidadBodega( self):
        return self.__cantidadBodega

    def getCantidadMinima(self):
        return self.__cantidadMinima

    def getCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setTipo(self, tipo):
        self.__tipo = tipo

    def vender(self, cantidad):
        if(cantidad <= self.__cantidadBodega):
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad

        else:
            print("Cantidad no disponible")

    def haySuficiente(self, cantidad):
        if cantidad <= self.__cantidadBodega:
            return True
        else:
            return False
        
    def getIVA(self):
        if self.__tipo == "PAPELERIA":
            return self.__IVA_PAPELERIA
        elif self.__tipo == "FARMACIA":
            return self.__IVA_FARMACIA
        elif self.__tipo == "SUPERMERCADO":
                return self.__IVA_SUPERMERCADO
        else:
            print ("Categoria no soportada")
    
    def subirValorUnitario(self):
        if self