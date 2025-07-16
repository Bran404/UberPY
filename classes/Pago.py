from classes.EnumEstadoPago import EstadoPago
from classes.EnumTipoViaje import TipoViaje
from classes.EnumMetodoPago import MetodoPago

class Pago:
    def __init__(self, metodoDePago: MetodoPago, tipoViaje: TipoViaje, subtotal: float = 5000):
        if metodoDePago not in MetodoPago:
            raise ValueError(f"Metodo de pago no valido: {metodoDePago}")
        self.__metodoDePago = metodoDePago
        self.__estadoPago = EstadoPago.PENDIENTE
        self.__tipoViaje = tipoViaje
        self.__subtotal = subtotal # Valor de ejemplo, logicamente el valor deberia de ser calculando la distancia del viaje

    @property
    def metodoDePago(self):
        return self.__metodoDePago
    
    @property
    def estadoPago(self):
        return self.__estadoPago

    @estadoPago.setter
    def estadoPago(self, estadoPago: EstadoPago)->None:
        if estadoPago in EstadoPago:
            self.__estadoPago = estadoPago

            print(f"Estado de pago actualizado: {self.__estadoPago}")
    
    @property
    def tipoViaje(self):
        return self.__tipoViaje
    
    def calcularTotal(self, cant_pasajeros:int)->int|float:

        print(f"Calculando total...")
        print(f"Precio base: {self.__subtotal}")
        match self.__tipoViaje:
            case TipoViaje.Individual:
                return self.__subtotal
            case TipoViaje.Compartido:
                self.__subtotal = self.__subtotal / cant_pasajeros
            case TipoViaje.Programado:
                self.__subtotal = self.__subtotal * 0.8
            case TipoViaje.Comfort:
                self.__subtotal = self.__subtotal * 2.0
            case TipoViaje.Rapido:
                self.__subtotal = self.__subtotal * 1.2
        
        print(f"Total calculado: {self.__subtotal}")
        
        return self.__subtotal