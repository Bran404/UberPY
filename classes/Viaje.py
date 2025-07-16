from classes.Chofer import Chofer
from classes.Pasajero import Pasajero
from classes.Pago import Pago
from classes.Direccion import Direccion
from classes.EnumTipoViaje import TipoViaje
from classes.EnumEstadoViaje import EstadoViaje
import random

class Viaje:

    __id=1
    def __init__(self, pasajeros: list[Pasajero], inicio: Direccion, fin: Direccion, tipoDeViaje: TipoViaje=None):
        self.__ID = str(Viaje.__id).zfill(5)
        Viaje.__id += 1
        self.__pasajeros = pasajeros
        self.__chofer = None
        self.__tipoDeViaje = tipoDeViaje or self.pasajeros[0].getTipoViaje()
        self.__comienzo = inicio
        self.__destinacion = fin
        self.__pago = Pago(self.pasajeros[0].metodoDePago, self.tipoDeViaje)
        self.__pago.calcularTotal(len(self.__pasajeros))
        self.__calificacion = 5     # Si no se califica, se asume que es porque no hubo críticas.
        self.__estadoViaje = EstadoViaje.SIN_CHOFER
        self.generarCodigoViaje()
    
    @property
    def ID(self)->str:
        return self.__ID

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

    @tipoDeViaje.setter
    def tipoDeViaje(self, tipoDeViaje:TipoViaje)->None:
        if tipoDeViaje in TipoViaje:
            self.__tipoDeViaje = tipoDeViaje
    
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

    @calificacion.setter
    def calificacion(self, calificacion:int)->None:
        if (calificacion <= 0 or calificacion >= 5) or not isinstance(calificacion, int):
            raise ValueError("La calificación debe estar entre 0 y 5")
        self.__calificacion = calificacion

    @property
    def estadoViaje(self)->EstadoViaje:
        return self.__estadoViaje

    @estadoViaje.setter
    def estadoViaje(self, estadoViaje:EstadoViaje)->None:
        if estadoViaje in EstadoViaje:
            self.__estadoViaje = estadoViaje

    @property
    def codigoViaje(self)->str:
        return self.__codigoViaje

    def cancelarViaje(self):        #FIXME: No se debe borrar la información del viaje. Se debe establecerlo como cancelado
        # self.pasajeros = []
        # self.chofer = None
        # self.tipoDeViaje = None
        # self.subTotal = None
        # self.calificacion = None
        # self.total = None
        self.__estadoViaje = EstadoViaje.CANCELADO
        print("Viaje cancelado exitosamente")

    def seguimientoViaje(self)->None:
        #Generacion de mensaje de seguimiento
        print("\nSeguimiento del viaje:")
        print(f"Tipo de viaje: {self.tipoDeViaje.value}")
        if not self.chofer:
            print("No hay chofer asignado al viaje.")
            return
        print(f"Viaje asignado a {self.chofer.nombre} con auto {self.chofer.auto.marca} {self.chofer.auto.modelo}.")
        print(f"Cantidad de pasajeros: {len(self.pasajeros)}")
    
    def asignarChofer(self, chofer: Chofer):
        if self.__chofer is not None:
            raise ValueError("El viaje ya tiene un chofer asignado")
        if not isinstance(chofer, Chofer):
            raise ValueError("El chofer debe ser una instancia de la clase Chofer")
        self.__chofer = chofer
    
    def generarCodigoViaje(self, longitud:int=4)->str:
        self.__codigoViaje = ''.join(random.choices('0123456789', k=longitud))

        print(f"Se ha creado el código {self.__codigoViaje} para viaje {self.__ID}.")