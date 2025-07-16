from classes.Historial import Historial
from classes.Auto import Auto
from classes.ZonaDeTrabajo import ZonaDeTrabajo

class Chofer():

    _id = 0
    def __init__(self, auto: Auto, nombre: str, zonasDeTrabajo: list[ZonaDeTrabajo]):
        self.__ID = Chofer._id
        Chofer._id += 1
        self.__auto = auto
        self.__nombre = nombre
        self.__zonasDeTrabajo = zonasDeTrabajo
        self.__available = False
        self.__historial = Historial()

    @property
    def ID(self):
        return self.__ID

    @property
    def auto(self):
        return self.__auto
    
    @auto.setter
    def auto(self, auto):
        self.__auto = auto
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def zonasDeTrabajo(self):
        return self.__zonasDeTrabajo

    @property
    def historial(self):
        for viaje in self.__historial.viajes:
            print(f"Total: {viaje.total}")
    
    @property
    def available(self):
        return self.__available
    
    @available.setter
    def available(self):
        self.__available = not self.__available

    def aceptarViaje(self, viaje):
        self.__historial.agregarViaje(viaje)
        self.__available = False

    def enviarCodigoViaje(self, code: str):
        "This is trashy code. Lo único que hace es devolver el code que se debería recibir desde una UI y devuelve el dato como si se tratara de un paso de fetch."
        return code