from pydantic import BaseModel
from typing import Optional

class EmpleadoSchema (BaseModel):
    id: Optional[int] = None
    ci_o_pasaporte: str
    nombres: str
    apellidos: str
    sexo: str = "M"
    telefono: int
    domicilio: str
    cargo: int
    usuario: int