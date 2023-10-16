from pydantic import BaseModel
from typing import Optional

class StockSchema (BaseModel):
    talla: int
    sucursal: int
    cantidad: int = 0