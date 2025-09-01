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
        self.__total = subtotal # Valor de ejemplo, logicamente el valor deberia de ser calculando la distancia del viaje

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

    @property
    def total(self)->int|float:
        return self.__total
    
    def calcularTotal(self, cant_pasajeros:int)->int|float:

        print(f"Calculando total...")
        print(f"Precio base: {self.__total}")
        match self.__tipoViaje:
            case TipoViaje.INDIVIDUAL:
                return self.__total
            case TipoViaje.COMPARTIDO:
                self.__total = self.__total / cant_pasajeros
            case TipoViaje.PROGRAMADO:
                self.__total = self.__total * 0.8
            case TipoViaje.COMFORT:
                self.__total = self.__total * 2.0
            case TipoViaje.RAPIDO:
                self.__total = self.__total * 1.2
        
        print(f"Total calculado: {self.__total}")
        
        return self.__total