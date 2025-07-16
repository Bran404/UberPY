from classes.Historial import Historial
from classes.Auto import Auto
from classes.ZonaDeTrabajo import ZonaDeTrabajo
from classes.Viaje import Viaje

class Chofer():

    _id = 1

    def __init__(self, Auto: Auto, nombre: str, zonasDeTrabajo: list[ZonaDeTrabajo]):
        self.__ID = str(Chofer._id).zfill(5)
        Chofer._id += 1
        self.__auto = Auto
        self.__nombre = nombre
        self.__zonasDeTrabajo = zonasDeTrabajo
        self.__available = False
        self.__historial = Historial()

        print(f"Chofer creado: {self.__nombre} ({self.__ID}).")

    """ @overload
    def __init__(self, marcaAuto:str, modeloAuto:str, nombre: str, zonasDeTrabajo: list[ZonaDeTrabajo]):
        self.__ID = str(Chofer._id).zfill(5)
        Chofer._id += 1
        self.__auto = Auto(marcaAuto, modeloAuto)
        self.__nombre = nombre
        self.__zonasDeTrabajo = zonasDeTrabajo
        self.__available = False
        self.__historial = Historial() """  #Unused. Sobrecarga para crear el auto por parámetros. Se reemplaza por solo invocar el constructor de Autos perse para evitar código dependiente.

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
    def available(self, value:bool):
        self.__available = value

        if self.__available:
            print(f"Chofer {self.__ID} ahora disponible.")
        else:
            print(f"Chofer {self.__ID} no disponible.")

    def aceptarViaje(self, viaje: Viaje):
        if not self.__available:
            raise ValueError("El chofer no esta disponible")
        self.__historial.agregarViaje(viaje)
        self.__available = False
        viaje.asignarChofer(self)

        print(f"Chofer {self.__ID} aceptó un nuevo viaje.")

    def enviarCodigoViaje(self, code: str):     #FIXME
        "This is trashy code. Lo único que hace es devolver el code que se debería recibir desde una UI y devuelve el dato como si se tratara de un paso de fetch."
        return code