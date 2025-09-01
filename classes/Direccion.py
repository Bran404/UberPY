class Direccion():
    def __init__(self, calle:str, altura:int):
        self.__calle=calle
        self.__altura=str(altura)

        print(f"Dirección creada: {self.__calle} {self.__altura}")

    @property
    def calle(self):
        return self.__calle

    @calle.setter
    def calle(self, nueva_calle:str):
        if nueva_calle.strip():
            self.__calle = nueva_calle.strip()
        else:
            raise ValueError("La calle no puede estar vacía")

    @property
    def altura(self):
        return self.__altura

    @altura.setter    
    def altura(self, nueva_altura:int):
        if nueva_altura is isinstance(int) and nueva_altura > 0:
            self.__altura = str(nueva_altura)
        else:
            raise ValueError("La altura debe ser un entero positivo")