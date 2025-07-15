from classes.Chofer import Chofer
from classes.Pasajero import Pasajero
from classes.Pago import Pago   
import random

class Viaje:
    def __init__(self, pasajeros: list[Pasajero], pago: Pago):
        self.pasajeros = pasajeros
        self.chofer = None
        self.tipoDeViaje = pago.getTipoViaje()
        self.subTotal = pago
        self.calificacion = None
        self.total = None
        self.codigoViaje = None

    def setCalificacionViaje(self, calificacion):
        if (calificacion < 0 or calificacion > 5):
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

    def seguimientoViaje(self):
        #Generacion de mensaje de seguimiento
        print("\nSeguimiento del viaje:")
        print(f"Tipo de viaje: {self.tipoDeViaje}")
        if not self.chofer:
            print("No hay chofer asignado al viaje.")
            return
        print(f"Viaje asignado a {self.chofer.nombre} con auto {self.chofer.auto.marca} {self.chofer.auto.modelo}.")
        print(f"Cantidad de pasajeros: {len(self.pasajeros)}")

    def calcularViaje(self):
        self.total = self.subTotal.calcularTotal(self.pasajeros)
        return self.total
    
    def asignarChofer(self, chofer: Chofer):
        if isinstance(chofer, Chofer):
            self.chofer = chofer
        else:
            raise ValueError("El chofer debe ser una instancia de la clase Chofer")
        
    def generarCodigoViaje(self, longitud=4):
        self.codigoViaje = ''.join(random.choices('0123456789', k=longitud))
        return self.codigoViaje