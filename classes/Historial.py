class Historial():
    def __init__(self):
        self.__viajes = []

    @property
    def viajes(self)->list:
        return self.__viajes
    
    @property
    def viaje(self, index:int):
        "Fetch the Viaje at the given index"
        return self.__viajes[index]

    def agregarViaje(self, viaje)->None:
        self.__viajes.append(viaje)

        print(f"Viaje {viaje.ID} agregado al historial.")