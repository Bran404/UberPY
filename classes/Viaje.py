from classes.Chofer import Chofer
from classes.Pasajero import Pasajero
from classes.Pago import Pago   

class Viaje:
    def __init__(self, pasajero: Pasajero, chofer: Chofer, destino, pago: Pago):
        self.pasajero = pasajero
        self.chofer = chofer
        self.tipoDeViaje = pago.getTipoViaje()
        self.destino = destino
        self.pago = pago
        self.calificacion = None