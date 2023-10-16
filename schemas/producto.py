from pydantic import BaseModel
from typing import Optional

class ProductoSchema (BaseModel):
    codigo: str
    descripcion: str
    precio: float
    descuento: Optional[int] = 0
    material: Optional[str] = None
    marca: int