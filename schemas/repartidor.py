from pydantic import BaseModel
from typing import Optional

class RepartidorSchema (BaseModel):
    id: Optional[int] = None
    placa: str
    descripcion_del_vehiculo: str
    foto_de_id: str = "default.jpg"
    foto_de_licencia_de_conducir: str = "default.jpg"
    foto_de_titulo_de_compra: str = "default.jpg"
    foto_de_poliza_de_seguro: str = "default.jpg"
    foto_de_SOAT: str = "default.jpg"
    empleado: int