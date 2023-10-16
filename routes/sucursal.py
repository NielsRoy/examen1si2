from fastapi import APIRouter, Response
from models.sucursal import Sucursal
from schemas.sucursal import SucursalSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

sucursal = APIRouter()

@sucursal.get("/sucursales", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Sucursal.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["direccion"] = data[1]
        dictionary["provincia"] = data[2]
        dictionary["departamento"] = data[3]
        dictionary["ubicacion_url"] = data[4]
        items.append(dictionary)
    return items

@sucursal.get("/sucursales/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Sucursal.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["direccion"] = data[1]
    dictionary["provincia"] = data[2]
    dictionary["departamento"] = data[3]
    dictionary["ubicacion_url"] = data[4]
    return dictionary

@sucursal.post("/sucursales", response_model=SucursalSchema, status_code=HTTP_201_CREATED)
def guardar(sucursal: SucursalSchema):
    data = sucursal.dict()
    data.pop("id")
    response = Sucursal.guardar(data)
    dictionary = {}
    dictionary["id"] = response[0]
    dictionary["direccion"] = response[1]
    dictionary["provincia"] = response[2]
    dictionary["departamento"] = response[3]
    dictionary["ubicacion_url"] = response[4]
    return dictionary

@sucursal.put("/sucursales/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, sucursal: SucursalSchema):
    data = sucursal.dict()
    data["id"] = id
    Sucursal.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@sucursal.delete("/sucursales/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar(id: int):
    Sucursal.eliminar(id)
    return Response(status_code=HTTP_204_NO_CONTENT)