class Direccion():
    def __init__(self, origen,destino):
        self.origen=origen
        self.destino = destino

    def getOrigen(self):
        return self.origen

    def setOrigen(self, nueva_origen):
        if nueva_origen:
            self._calle = nueva_origen
        else:
            raise ValueError("La calle no puede estar vacía")
        
    def getDestino(self):
        return self.destino