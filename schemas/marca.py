from pydantic import BaseModel
from typing import Optional

class MarcaSchema (BaseModel):
    id: Optional[int] = None
    nombre: str