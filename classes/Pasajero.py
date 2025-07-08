import Direccion

class Pasajero:
    def __init__(self, nombre):
        self.nombre=nombre
        self.direcciones=[]

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombreNuevo):
        self.nombre=nombreNuevo

    def agregarDireccion(self, direccionNueva: Direccion):
        if isinstance(direccionNueva, Direccion):
            self.direcciones.append(direccionNueva)
        else:
            raise ValueError("Dirección no válida")

    def getDirecciones(self):
        for direccion in self.direcciones:
            print(direccion.getCalle())