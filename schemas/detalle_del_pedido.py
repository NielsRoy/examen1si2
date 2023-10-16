from pydantic import BaseModel
from typing import Optional

class DetalleDelPedidoSchema (BaseModel):
    producto: str
    cantidad: int = 1