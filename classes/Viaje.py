from classes.Chofer import Chofer
from classes.Pasajero import Pasajero
from classes.Pago import Pago   

class Viaje:
    def __init__(self, pasajero: Pasajero, chofer: Chofer, pago: Pago):
        self.pasajeros = []
        self.pasajeros.append(pasajero)
        self.chofer = chofer
        self.tipoDeViaje = pago.getTipoViaje()
        self.subTotal = pago
        self.calificacion = None
        self.total = None

    def setCalificacionViaje(self, calificacion):
        if (calificacion < 0 or calificacion > 5) and (calificacion.is_integer() == False):
            raise ValueError("La calificación debe estar entre 0 y 5")
        self.calificacion = calificacion 
        return self.calificacion

    def cancelarViaje(self):
        self.pasajeros = []
        self.chofer = None
        self.tipoDeViaje = None
        self.subTotal = None
        self.calificacion = None
        self.total = None
        print("Viaje cancelado exitosamente")
    
    def seguimientoViaje():
        pass

    def calcularViaje(self):
        self.total = self.subTotal.calcularTotal(self.pasajeros)
        return self.total