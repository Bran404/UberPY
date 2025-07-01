from classes.Historial import Historial
from classes.Auto import Auto
from classes.ZonaDeTrabajo import ZonaDeTrabajo

class Chofer():

    Chofer__id = 0
    def __init__(self, auto: Auto, nombre: str, zonasDeTrabajo: list[ZonaDeTrabajo]):
        self.ID = Chofer.__id
        Chofer.__id += 1
        self.__auto = auto
        self.__nombre = nombre
        self.__zonasDeTrabajo = zonasDeTrabajo
        self.__available = False
        self.__historial = Historial()

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
        return self.__historial
    
    @property
    def available(self):
        return self.__available
    
    @available.setter
    def available(self):
        self.__available = not self.__available