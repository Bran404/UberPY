from classes.EnumEstadoPago import EstadoPago
from classes.EnumTipoViaje import TipoViaje
from classes.EnumMetodoPago import MetodoPago
from classes.Pasajero import Pasajero

class Pago:
    def __init__(self, metodoDePago: MetodoPago, tipoViaje: TipoViaje):
        if metodoDePago not in MetodoPago:
            raise ValueError(f"Metodo de pago no valido: {metodoDePago}")
        self.__metodoDePago = metodoDePago
        self.__estadoPago = EstadoPago.PENDIENTE
        self.__tipoViaje = tipoViaje
        self.__subtotal = self.subtotal = 5000 # Valor de ejemplo, logicamente el valor deberia de ser calculando la distancia del viaje

    @property
    def metodoDePago(self):
        return self.__metodoDePago
    
    @property
    def estadoPago(self):
        return self.__estadoPago
    
    @property
    def tipoViaje(self):
        return self.__tipoViaje
    
    def calcularTotal(self, pasajeros: list[Pasajero]):
        match self.__tipoViaje:
            case TipoViaje.Individual:
                total = self.__subtotal
            case TipoViaje.Compartido:
                total = self.__subtotal / len(pasajeros)
            case TipoViaje.Programado:
                total = self.__subtotal * 0.8
            case TipoViaje.Comfort:
                total = self.__subtotal * 2.0
            case TipoViaje.Rapido:
                total = self.__subtotal * 1.2
            case _:
                total = self.__subtotal     # Error case. Se calcula individual
        return total