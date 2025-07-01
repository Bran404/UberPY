class Pago:

    def __init__(self, id_pago, monto, metodo_pago):
        self.id_pago = id_pago
        self.monto = monto
        self.metodo_pago = metodo_pago  # "efectivo", "tarjeta", etc.
        self.estado = "pendiente"
        self.fecha_pago = None

    def calcular_pago(self):
        

    def realizar_pago(self):
        if self.metodo_pago in ["efectivo", "tarjeta", "Billetera virtual"]:
            self.estado = "completado"
            self.fecha_pago = datetime.now()
            print(f"Pago de ${self.monto} realizado exitosamente.")
        else:
            self.estado = "fallido"
            print("Método de pago no válido.")

    def verificar_estado(self):
        return f"Estado del pago: {self.estado}"

    def cancelar_pago(self):
        if self.estado == "pendiente":
            self.estado = "cancelado"
            print("Pago cancelado.")
        else:
            print("No se puede cancelar un pago ya procesado.")