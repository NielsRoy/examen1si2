from fastapi import APIRouter, Response
from models.privilegio import Privilegio
from schemas.privilegio import PrivilegioSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

privilegio = APIRouter()

@privilegio.get("/privilegios", status_code=HTTP_200_OK)
def mostrar_todos():
    items = []
    for data in Privilegio.obtener_todos():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["descripcion"] = data[1]
        items.append(dictionary)
    return items

@privilegio.get("/privilegios/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Privilegio.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["descripcion"] = data[1]
    return dictionary

@privilegio.put("/privilegios/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, privilegio: PrivilegioSchema):
    data = privilegio.dict()
    data["id"] = id
    Privilegio.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)