from enum import Enum

class EstadoPago(Enum):
    PAGADO = "Pagado"
    EN_PROCESO = "En proceso"
    PENDIENTE = "Pendiente"
    DENEGADO = "Denegado"