from classes.EnumTipoViaje import TipoViaje as Values

class TipoViaje:
    def __init__(self, tipoViaje: Values):
        if tipoViaje not in Values:
            raise ValueError("Tipo de viaje no válido.")
        self.tipoViaje = tipoViaje

    def getTipoViaje(self):
        return self.tipoViaje

    def setTipoViaje(self, tipoViaje: Values):
        self.tipoViaje = tipoViaje
