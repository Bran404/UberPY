from Direccion import Direccion

class Pasajero:
    def __init__(self, nombre, direccion:Direccion):
        self.__nombre=nombre
        self.direccion=direccion

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombreNuevo):
        self.nombre=nombreNuevo