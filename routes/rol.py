from fastapi import APIRouter, Response
from models.rol import Rol
from schemas.rol import RolSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

rol = APIRouter()

@rol.get("/roles", status_code=HTTP_200_OK)
def mostrar_todos():
    items = []
    for data in Rol.obtener_todos():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        items.append(dictionary)
    return items

@rol.get("/roles/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Rol.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["nombre"] = data[1]
    return dictionary

@rol.post("/roles", response_model=RolSchema, status_code=HTTP_201_CREATED)
def guardar(rol: RolSchema):
    data = rol.dict()
    data.pop("id")
    response = Rol.guardar(data)
    dictionary = {}
    dictionary["id"] = response[0]
    dictionary["nombre"] = response[1]
    return dictionary

@rol.put("/roles/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, rol: RolSchema):
    data = rol.dict()
    data["id"] = id
    Rol.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@rol.delete("/roles/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar(id: int):
    Rol.eliminar(id)
    return Response(status_code=HTTP_204_NO_CONTENT)


@rol.get("/roles/{id}/privilegios", status_code=HTTP_200_OK)
def mostrar_privilegios(id: int):
    items = []
    for data in Rol.obtener_privilegios(id):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["descripcion"] = data[1]
        items.append(dictionary)
    return items

@rol.post("/roles/{id}/privilegios", status_code=HTTP_204_NO_CONTENT)
def asignar_privilegios(id: int, privilegios: list[int]):  #privilegios como lista de int
    Rol.asignar_privilegios(id, privilegios)
    return Response(status_code=HTTP_204_NO_CONTENT)

@rol.delete("/roles/{id}/privilegios", status_code=HTTP_204_NO_CONTENT)
def quitar_privilegios(id: int, privilegios: list[int]):
    Rol.quitar_privilegios(id, privilegios)
    return Response(status_code=HTTP_204_NO_CONTENT)