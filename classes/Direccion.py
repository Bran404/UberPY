from Pasajero import Pasajero

class Direccion():
    def __init__(self, calle, persona:Pasajero):
        self.persona=persona
        self.calle=calle

    def getCalle(self):
        return self._calle

    def setCalle(self, nueva_calle):
        if nueva_calle:
            self._calle = nueva_calle
        else:
            raise ValueError("La calle no puede estar vacía")

    def getPersona(self):
        return self._persona