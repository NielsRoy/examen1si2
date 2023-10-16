from pydantic import BaseModel
from typing import Optional

from datetime import date, time

class PedidoSchema (BaseModel):
    nro: Optional[int] = None
    fecha: date
    hora: time
    cliente: int
    repartidor: Optional[int] = None
    direccion_de_entrega: int
    completado: bool = False