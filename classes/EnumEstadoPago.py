from enum import Enum

class EstadoPago(Enum):
    PAGADO = "PAGADO"
    EN_PROCESO = "EN_PROCESO"
    PENDIENTE = "PENDIENTE"
    DENEGADO = "DENEGADO"