from pydantic import BaseModel
from typing import Optional

class DireccionSchema (BaseModel):
    id: Optional[int] = None
    nombre: str
    descripcion: str
    provincia: str
    departamento: str
    url: str
    cliente: int