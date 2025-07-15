from classes.Viaje import Viaje

class CanlificaionViaje:
    def __init__(self, viaje:Viaje):
        self.__pasajero = viaje.pasajeros[0]
        self.__conductor = viaje.chofer
        self.__calificacion_conductor #Sera de 1 a 5 estrellas
        self.__comentario

    def set_calificacion_conductor(self, estrellas):
        if isinstance(estrellas, int) and 1 <= estrellas <= 5:
            self.__calificacion_conductor = estrellas
        else:
            raise ValueError("La calificacion debe ser un numero entre 1 y 5")

    def agregar_comentario(self, comentario):
        if isinstance(comentario, str) and comentario.strip():
            self.__comentario = comentario.strip()
        else:
            raise ValueError("El comentario no puede estar vacío") 

    def mostrarCalificacion(self):
        if self.__calificacion_conductor:
            return f"{self.__pasajero} califico al chofer {self.__conductor} con {self.__calificacion_conductor} estrellas."
        return "aun no se a calificado al chofer."
    
    def mostrarComentario(self):
        if self.__comentario:
            return f"Comentario: {self.__comentario}"
        return "No hay comentarios."
