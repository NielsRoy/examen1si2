from fastapi import APIRouter, Response
from models.categoria import Categoria
from schemas.categoria import CategoriaSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

categoria = APIRouter()

@categoria.get("/categorias", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Categoria.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        items.append(dictionary)
    return items

@categoria.get("/categorias/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Categoria.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["nombre"] = data[1]
    return dictionary

@categoria.post("/categorias", response_model=CategoriaSchema, status_code=HTTP_201_CREATED)
def guardar(categoria: CategoriaSchema):
    data = categoria.dict()
    data.pop("id")
    response = Categoria.guardar(data)
    dictionary = {}
    dictionary["id"] = response[0]
    dictionary["nombre"] = response[1]
    return dictionary

@categoria.put("/categorias/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, categoria: CategoriaSchema):
    data = categoria.dict()
    data["id"] = id
    Categoria.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@categoria.delete("/categorias/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar(id: int):
    Categoria.eliminar(id)
    return Response(status_code=HTTP_204_NO_CONTENT)