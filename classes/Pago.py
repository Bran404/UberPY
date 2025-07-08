import EnumEstadoPago
import EnumTipoViaje

class Pago:
    def __init__(self, metodoDePago, tipoViaje,subtotal):
        self.metodoDePago = metodoDePago
        self.estadoPago = EnumEstadoPago.EstadoPago.PENDIENTE
        self.tipoViaje = EnumTipoViaje.TipoViaje(tipoViaje)
        self.subtotal = subtotal

    def getMetodoPago(self):
        return self.metodoDePago
    
    def getEstadoPago(self):
        return self.estadoPago
    
    def getTipoViaje(self):
        return self.tipoViaje
    
    def calcularTotal(self, pasajeros):
        if self.tipoViaje == "Individual":
            total = self.subtotal
        elif self.tipoViaje == "Compartido":
            total = self.subtotal / len(pasajeros)
        elif self.tipoViaje == "Programado":
            total = self.subtotal * 0.8
        elif self.tipoViaje == "Comfort":
            total = self.subtotal * 2.0
        elif self.tipoViaje == "Rapido":
            total = self.subtotal * 1.2
        return total