class ZonaDeTrabajo():
    ZonaDeTrabajo.__codeList = []

    def __init__(self, codigo: str):
        self.__codigo = ZonaDeTrabajo.__set_codigo(codigo)

    @property
    def codigo(self):
        return self.__codigo
    
    @staticmethod
    def __set_codigo(codigo: str):
        if codigo in ZonaDeTrabajo.__codeList:
            return ZonaDeTrabajo.__codeList.index(codigo)
        else:
            ZonaDeTrabajo.__codeList.append(codigo)
            return ZonaDeTrabajo.__codeList.index(codigo)