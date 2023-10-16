from pydantic import BaseModel
from typing import Optional

class TallaSchema (BaseModel):
    id: Optional[int] = None
    nombre: str