from fastapi import APIRouter, Response
from models.talla import Talla
from schemas.talla import TallaSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

talla = APIRouter()

@talla.get("/tallas", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Talla.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        items.append(dictionary)
    return items

@talla.get("/tallas/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Talla.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["nombre"] = data[1]
    return dictionary

@talla.post("/tallas", response_model=TallaSchema, status_code=HTTP_201_CREATED)
def guardar(talla: TallaSchema):
    data = talla.dict()
    data.pop("id")
    response = Talla.guardar(data)
    dictionary = {}
    dictionary["id"] = response[0]
    dictionary["nombre"] = response[1]
    return dictionary

@talla.put("/tallas/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, talla: TallaSchema):
    data = talla.dict()
    data["id"] = id
    Talla.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@talla.delete("/tallas/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar(id: int):
    Talla.eliminar(id)
    return Response(status_code=HTTP_204_NO_CONTENT)