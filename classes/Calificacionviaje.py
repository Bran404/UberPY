class Calificarviaje:
    def __init__(self, pasajero, conductor):
        self.pasajero = pasajero
        self.conductor = conductor
        self.calificacion_conductor = None #Sera de 1 a 5 estrellas
        self.comentario = none 

    def set_calificacion_conductor(self, estrellas):
        if isinstance(estrellas, int) and 1 <= estrellas <= 5:
            self.calificacion_conductor = estrellas
        else:
            raise ValueError("La calificacion debe ser un numero entre 1 y 5")

    def agregar_comentario(self, comentario):
        if isinstance(comentario, str) and comentario.strip():
            self.comentario = comentario.strip()
        else:
            raise ValueError("El comentario no puede estar vacio") 

    def mostrarCalificacion(self):
        if self.calificacion_conductor:
            return f"{self.pasajero} califico al chofer {self.conductor} con {self.calificacion_conductor} estrellas."
        return "aun no se a calificado al chofer."
    
    def mostrarComentario(self):
        if self.comentario:
            return f"Comentario: {self.comentario}"
        return "No hay comentarios."
