from pydantic import BaseModel
from typing import Optional

class PrivilegioSchema (BaseModel):
    id: Optional[int] = None
    descripcion: str