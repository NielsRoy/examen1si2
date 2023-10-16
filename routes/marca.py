from fastapi import APIRouter, Response
from models.marca import Marca
from schemas.marca import MarcaSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

marca = APIRouter()

@marca.get("/marcas", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Marca.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        items.append(dictionary)
    return items

@marca.get("/marcas/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Marca.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["nombre"] = data[1]
    return dictionary

@marca.post("/marcas", response_model=MarcaSchema, status_code=HTTP_201_CREATED)
def guardar(marca: MarcaSchema):
    data = marca.dict()
    data.pop("id")
    response = Marca.guardar(data)
    dictionary = {}
    dictionary["id"] = response[0]
    dictionary["nombre"] = response[1]
    return dictionary

@marca.put("/marcas/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, marca: MarcaSchema):
    data = marca.dict()
    data["id"] = id
    Marca.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@marca.delete("/marcas/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar(id: int):
    Marca.eliminar(id)
    return Response(status_code=HTTP_204_NO_CONTENT)