class CalificacionViaje:
    def __init__(self):
        self.__calificacion_conductor #Sera de 1 a 5 estrellas
        self.__comentario 

    @property
    def calificacion(self):
        if self.__calificacion_conductor:
            return f"{self.__pasajero} califico al chofer {self.__conductor} con {self.__calificacion_conductor} estrellas."
        return "aun no se a calificado al chofer en este viaje."
    
    @calificacion.setter
    def calificacion(self, estrellas):
        if isinstance(estrellas, int) and 1 <= estrellas <= 5:
            self.__calificacion_conductor = estrellas
        else:
            raise ValueError("La calificacion debe ser un numero entre 1 y 5")
        
    @property
    def comentario(self):
        if self.__comentario:
            return f"Comentario: {self.__comentario}"
        return "No hay comentarios."

    @comentario.setter
    def comentario(self, comentario):
        if isinstance(comentario, str) and comentario.strip():
            self.__comentario = comentario.strip()
        else:
            raise ValueError("El comentario no puede estar vacío")