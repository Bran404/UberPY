from classes.EnumEstadoPago import EstadoPago
from classes.EnumTipoViaje import TipoViaje
from classes.MetodoPago import MetodoPago
class Pago:
    def __init__(self, metodoDePago: MetodoPago, tipoViaje):
        self.metodoDePago = metodoDePago
        self.estadoPago = EstadoPago.PENDIENTE.value
        self.tipoViaje = tipoViaje
        self.subtotal = 5000 # Valor de ejemplo, logicamente el valor deberia de ser calculando la distancia del viaje 

    def getMetodoPago(self):
        return self.metodoDePago.MetodoPago()
    
    def getEstadoPago(self):
        return self.estadoPago
    
    def getTipoViaje(self):
        return self.tipoViaje.getTipoViaje()
    
    def calcularTotal(self, pasajeros):
        tipo = self.tipoViaje.getTipoViaje()
        print(f"- Calculando total para {len(pasajeros)} pasajeros")
        print(f"- Calculando total para un viaje {tipo}")
        if tipo == TipoViaje.Individual.value:
            total = self.subtotal
        elif tipo == TipoViaje.Compartido.value:
            print(f"- Cantidad de pasajeros: {len(pasajeros)}")
            total = self.subtotal / len(pasajeros)
        elif tipo == TipoViaje.Programado.value:
            total = self.subtotal * 0.8
        elif tipo == TipoViaje.Comfort.value:
            total = self.subtotal * 2.0
        elif tipo == TipoViaje.Rapido.value:
            total = self.subtotal * 1.2
        return total