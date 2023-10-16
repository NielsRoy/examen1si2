from pydantic import BaseModel
from typing import Optional

class ClienteSchema (BaseModel):
    id: Optional[int] = None
    nombres: str
    apellidos: str
    telefono: int
    sexo: str = "M"
    usuario: int