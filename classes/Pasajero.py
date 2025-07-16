from classes.Direccion import Direccion
from EnumMetodoPago import MetodoPago

class Pasajero:

    _id = 1
    def __init__(self, nombre, metodoDePago: MetodoPago=MetodoPago.EFECTIVO):
        self.__ID = str(Pasajero._id).zfill(5)
        Pasajero._id += 1
        self.__nombre=nombre
        self.__direcciones:list[Direccion]=[]
        self.__metodoDePago=metodoDePago

        print(f"Pasajero creado: {self.__nombre} ({self.__ID}).")
    
    @property
    def ID(self)->str:
        return self.__ID

    @property
    def nombre(self)->str:
        return self.__nombre

    @property
    def metodoDePago(self)->MetodoPago:
        return self.__metodoDePago

    @metodoDePago.setter
    def nombre(self, nombreNuevo:str)->None:
        self.__nombre=nombreNuevo

    @property
    def direcciones(self)->list[Direccion]:
        return self.__direcciones

    def agregarDireccion(self, direccionNueva: Direccion)->None:
        if isinstance(direccionNueva, Direccion):
            self.__direcciones.append(direccionNueva)

            print(f"Dirección agregada: {direccionNueva.calle} {direccionNueva.altura} a pasajero {self.__ID}.")
        else:
            raise ValueError("Dirección no válida")