from pydantic import BaseModel
from typing import Optional

class CargoSchema (BaseModel):
    id: Optional[int] = None
    nombre: str