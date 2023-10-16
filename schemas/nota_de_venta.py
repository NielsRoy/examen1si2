from pydantic import BaseModel
from typing import Optional

from datetime import date, time

class NotaDeVentaSchema (BaseModel):
    nro: Optional[int] = None
    fecha: date
    hora: time
    monto: float
    descuento: int
    monto_final: float
    cliente: int