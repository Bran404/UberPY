from EnumTipoViaje import TipoViaje

class TipoViaje:
    def __init__(self, tipoViaje: TipoViaje):
        if tipoViaje not in TipoViaje:
            raise ValueError(f"Tipo de viaje no válido: {tipoViaje}")
        self.tipoViaje = tipoViaje

    def setTipoViaje(self, tipoViaje: TipoViaje):
        self.tipoViaje = tipoViaje
