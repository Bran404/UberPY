class ZonaDeTrabajo():
    _codeList = []

    def __init__(self, codigo: str):
        self.__codigo = ZonaDeTrabajo.__set_codigo(codigo)

    @property
    def codigo(self):
        return self.__codigo
    
    @staticmethod
    def __set_codigo(codigo: str):
        if codigo in ZonaDeTrabajo._codeList:
            return ZonaDeTrabajo._codeList.index(codigo)
        else:
            ZonaDeTrabajo._codeList.append(codigo)
            return ZonaDeTrabajo._codeList.index(codigo)