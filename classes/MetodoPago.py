from classes.EnumMetodoPago import MetodoPago as Values

class MetodoPago:
    def __init__(self, metodoPago: Values):
        if metodoPago not in Values:
            raise ValueError(f"Metodo de pago no válido.")
        self.metodoPago = metodoPago

    def MetodoPago(self):
        return self.metodoPago