from pydantic import BaseModel
from typing import Optional

class SucursalSchema (BaseModel):
    id: Optional[int] = None
    direccion: str
    provincia: str
    departamento: str
    ubicacion_url: str