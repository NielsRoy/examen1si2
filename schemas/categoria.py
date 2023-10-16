from pydantic import BaseModel
from typing import Optional

class CategoriaSchema (BaseModel):
    id: Optional[int] = None
    nombre: str