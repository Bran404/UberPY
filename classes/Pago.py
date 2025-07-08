import EnumEstadoPago
import TipoViaje

class Pago:
    def __init__(self, metodoDePago, tipoViaje,subtotal):
        self.metodoDePago = metodoDePago
        self.estadoPago = EnumEstadoPago.EstadoPago.PENDIENTE
        self.tipoViaje = TipoViaje.TipoViaje(tipoViaje)
        self.subtotal = subtotal

    def getMetodoPago(self):
        return self.metodoDePago
    
    def getEstadoPago(self):
        return self.estadoPago
    
    def getTipoViaje(self):
        return self.tipoViaje
    
    def calcularTotal(self):
        if self.tipoViaje == "NORMAL":
            total = self.subtotal
        elif self.tipoViaje == "PREMIUM":
            total = self.subtotal * 1.5
        elif self.tipoViaje == "ECONOMICO":
            total = self.subtotal * 0.8
        return total