from pydantic import BaseModel
from typing import Optional

class UsuarioSchema (BaseModel):
    id: Optional[int] = None
    email: str
    clave: str
    foto: Optional[str] = None
    rol: int