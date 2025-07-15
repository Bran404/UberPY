from classes.Direccion import Direccion
from EnumMetodoPago import MetodoPago

class Pasajero:
    def __init__(self, nombre, metodoDePago: MetodoPago=MetodoPago.EFECTIVO):
        self.__nombre=nombre
        self.__direcciones=[]
        self.__metodoDePago=metodoDePago

    @property
    def nombre(self):
        return self.__nombre

    @property
    def metodoDePago(self):
        return self.__metodoDePago

    @metodoDePago.setter
    def nombre(self, nombreNuevo):
        self.__nombre=nombreNuevo

    @property
    def direcciones(self):
        return self.__direcciones

    @direcciones.setter
    def agregarDireccion(self, direccionNueva: Direccion):
        if isinstance(direccionNueva, Direccion):
            self.__direcciones.append(direccionNueva)
        else:
            raise ValueError("Dirección no válida")