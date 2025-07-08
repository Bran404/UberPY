from EnumMetodoPago import MetodoPago

class MetodoPago:
    def __init__(self, metodoPago: MetodoPago):
        if metodoPago not in MetodoPago:
            raise ValueError(f"Metodo de pago no válido: {metodoPago}")
        self.metodoPago = metodoPago

    def MetodoPago(self):
        return self.metodoPago