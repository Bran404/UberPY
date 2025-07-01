class Calificarviaje:
    def __init__(self, pasajero, conductor):
        self.pasajero = pasajero
        self.conductor = conductor
        self.calificacion_conductor = None #Sera de 1 a 5 estrellas

    def set_calificacion_conductor(self, estrellas):
        self.calificacion_conductor = estrellas
        