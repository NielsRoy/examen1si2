from fastapi import APIRouter, Response
from models.cliente import Cliente
from schemas.cliente import ClienteSchema
from schemas.direccion import DireccionSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

cliente = APIRouter()

@cliente.get("/clientes", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Cliente.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["nombres"] = data[1]
        dictionary["apellidos"] = data[2]
        dictionary["telefono"] = data[3]
        dictionary["sexo"] = data[4]
        dictionary["usuario"] = data[5]
        items.append(dictionary)
    return items

@cliente.get("/clientes/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Cliente.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["nombres"] = data[1]
    dictionary["apellidos"] = data[2]
    dictionary["telefono"] = data[3]
    dictionary["sexo"] = data[4]
    dictionary["usuario"] = data[5]
    return dictionary

@cliente.post("/clientes", response_model=ClienteSchema, status_code=HTTP_201_CREATED)
def guardar(cliente: ClienteSchema):
    data = cliente.dict()
    data.pop("id")
    response = Cliente.guardar(data)
    dictionary = {}
    dictionary["id"] = response[0]
    dictionary["nombres"] = response[1]
    dictionary["apellidos"] = response[2]
    dictionary["telefono"] = response[3]
    dictionary["sexo"] = response[4]
    dictionary["usuario"] = response[5]
    return dictionary

@cliente.put("/clientes/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, cliente: ClienteSchema):
    data = cliente.dict()
    data["id"] = id
    Cliente.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@cliente.delete("/clientes/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar(id: int):
    Cliente.eliminar(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@cliente.get("/clientes/{id}/direcciones", status_code=HTTP_200_OK)
def mostrar_direcciones(id: int):
    items = []
    for data in Cliente.obtener_direcciones(id):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["nombre"] = data[1]
        dictionary["descripcion"] = data[2]
        dictionary["provincia"] = data[3]
        dictionary["departamento"] = data[4]
        dictionary["url"] = data[5]
        dictionary["cliente"] = data[6]
        items.append(dictionary)
    return items

@cliente.post("/direcciones", status_code=HTTP_201_CREATED)
def agregar_direccion(direccion: DireccionSchema):
    data = direccion.dict()
    data.pop("id")
    Cliente.agregar_direccion(data)
    return Response(status_code=HTTP_201_CREATED)

@cliente.put("/direcciones/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar_direccion(id: int, direccion: DireccionSchema):
    data = direccion.dict()
    data["id"] = id
    Cliente.actualizar_direccion(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@cliente.delete("/direcciones/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar_direccion(id: int):
    Cliente.eliminar_direccion(id)
    return Response(status_code=HTTP_204_NO_CONTENT)


