from classes.Chofer import Chofer
from classes.Pasajero import Pasajero
from classes.Pago import Pago
from classes.Direccion import Direccion
from classes.EnumTipoViaje import TipoViaje
from classes.enumEstadoPago import EstadoPago
import random

class Viaje:
    def __init__(self, pasajeros: list[Pasajero], inicio: Direccion, fin: Direccion, tipoDeViaje: TipoViaje=None):
        self.__pasajeros = pasajeros
        self.__chofer
        self.__tipoDeViaje = tipoDeViaje or self.pasajeros[0].getTipoViaje()
        self.__comienzo = inicio
        self.__destinacion = fin
        self.__pago = Pago(self.pasajeros[0].getMetodoPago(), self.tipoDeViaje, self.calcularViaje())
        self.__calificacion

    def setCalificacionViaje(self, calificacion:int):
        if (calificacion <= 0 or calificacion >= 5) or (calificacion.is_integer() == False):
            raise ValueError("La calificación debe estar entre 0 y 5")
        self.__calificacion = calificacion

    def cancelarViaje(self):        #FIXME: No se debe borrar la infomación del viaje. Se debe establecerlo como cancelado
        # self.pasajeros = []
        # self.chofer = None
        # self.tipoDeViaje = None
        # self.subTotal = None
        # self.calificacion = None
        # self.total = None
        print("Viaje cancelado exitosamente")

    def seguimientoViaje(self):
        #Generacion de mensaje de seguimiento
        print("\nSeguimiento del viaje:")
        print(f"Tipo de viaje: {self.tipoDeViaje}")
        if not self.chofer:
            print("No hay chofer asignado al viaje.")
            return
        print(f"Viaje asignado a {self.chofer.nombre} con auto {self.chofer.auto.marca} {self.chofer.auto.modelo}.")
        print(f"Cantidad de pasajeros: {len(self.pasajeros)}")

    def calcularViaje(self):        #FIXME: Esta función es ilógica
        self.total = self.__pago.calcularTotal(self.pasajeros)
        return self.total
    
    def asignarChofer(self, chofer: Chofer):
        if self.__chofer is not None:
            raise ValueError("El viaje ya tiene un chofer asignado")
        if not isinstance(chofer, Chofer):
            raise ValueError("El chofer debe ser una instancia de la clase Chofer")
        self.__chofer = chofer

    
    @property
    def pasajeros(self)->list[Pasajero]:
        return self.__pasajeros
    
    @property
    def chofer(self)->Chofer:
        if not self.__chofer:
            return None
        return self.__chofer
    
    @property
    def tipoDeViaje(self)->TipoViaje:
        return self.__tipoDeViaje
    
    @property
    def comienzo(self)->Direccion:
        return self.__comienzo
    
    @property
    def destinacion(self)->Direccion:
        return self.__destinacion
    
    @property
    def pago(self)->Pago:
        return self.__pago
    
    @property
    def calificacion(self)->int:
        return self.__calificacion

        
    def generarCodigoViaje(self, longitud:int=4):
        self.codigoViaje = ''.join(random.choices('0123456789', k=longitud))
        return self.codigoViaje
    
    def setEstadoViaje(self, estado):
        self.estadoViaje = estado
        return self.estadoViaje