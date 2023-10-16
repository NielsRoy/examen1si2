from pydantic import BaseModel
from typing import Optional

class DetalleDeVentaSchema (BaseModel):
    nota_de_venta: Optional[int] = None
    producto: str
    cantidad: int = 1
    monto: float
    descuento: int