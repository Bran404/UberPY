from enum import Enum

class EstadoViaje(Enum):
    SIN_CHOFER="Sin chofer"
    PENDIENTE_ACEPTAR_CHOFER="Pendiente de aceptar chofer"
    CHOFER_EN_CAMINO="Chofer en camino"
    REQUIERE_CONFIRMACION="Requiere confirmación del código de viaje"
    EN_RUTA="En ruta"
    FINALIZADO="Finalizado"
    CANCELADO="Cancelado"