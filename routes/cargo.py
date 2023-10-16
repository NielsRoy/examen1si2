from fastapi import APIRouter, Response
from models.cargo import Cargo
from schemas.cargo import CargoSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

cargo = APIRouter()

@cargo.get("/cargos", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Cargo.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        items.append(dictionary)
    return items

@cargo.get("/cargos/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Cargo.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["nombre"] = data[1]
    return dictionary

@cargo.post("/cargos", response_model=CargoSchema, status_code=HTTP_201_CREATED)
def guardar(cargo: CargoSchema):
    data = cargo.dict()
    data.pop("id")
    response = Cargo.guardar(data)
    dictionary = {}
    dictionary["id"] = response[0]
    dictionary["nombre"] = response[1]
    return dictionary

@cargo.put("/cargos/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, cargo: CargoSchema):
    data = cargo.dict()
    data["id"] = id
    Cargo.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@cargo.delete("/cargos/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar(id: int):
    Cargo.eliminar(id)
    return Response(status_code=HTTP_204_NO_CONTENT)