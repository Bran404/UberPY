class Historial():
    def __init__(self):
        self.__viajes = []

    @property
    def viajes(self):
        return self.__viajes
    
    @property
    def viaje(self, index):
        return self.__viajes[index]

    def agregarViaje(self, viaje):
        self.__viajes.append(viaje)