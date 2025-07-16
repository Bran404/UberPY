class Auto():
    def __init__(self, marca: str, modelo: str):
        self.__marca = marca
        self.__modelo = modelo

        print(f"Auto creado: {self.__marca} {self.__modelo}")

    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo