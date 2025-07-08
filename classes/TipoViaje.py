from enum import Enum

class TipoViaje(Enum):
    NORMAL = "NORMAL"
    PREMIUM = "PREMIUM"
    ECONOMICO = "ECONOMICO"
    COMPARTIDO = "COMPARTIDO"

    # FIXME: #2 Los tipos deben ser: Individual, Compartido, Programado, Comfort, Rápido