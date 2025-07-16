from classes.Viaje import Viaje #Esto sólo es para que el IDE lo reconozca

class Historial():
    def __init__(self):
        self.__viajes = []

    @property
    def viajes(self)->list[Viaje]:
        return self.__viajes
    
    @property
    def viaje(self, index:int)->Viaje:
        "Fetch the Viaje at the given index"
        return self.__viajes[index]

    def agregarViaje(self, viaje:Viaje)->None:
        self.__viajes.append(viaje)

        print(f"Viaje {viaje.ID} agregado al historial.")