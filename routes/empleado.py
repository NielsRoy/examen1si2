from fastapi import APIRouter, Response
from models.empleado import Empleado
from schemas.empleado import EmpleadoSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

empleado = APIRouter()

@empleado.get("/empleados", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Empleado.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["ci_o_pasaporte"] = data[1]
        dictionary["nombres"] = data[2]
        dictionary["apellidos"] = data[3]
        dictionary["sexo"] = data[4]
        dictionary["telefono"] = data[5]
        dictionary["domicilio"] = data[6]
        dictionary["cargo"] = data[7]
        dictionary["usuario"] = data[8]
        items.append(dictionary)
    return items

@empleado.get("/empleados/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Empleado.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["ci_o_pasaporte"] = data[1]
    dictionary["nombres"] = data[2]
    dictionary["apellidos"] = data[3]
    dictionary["sexo"] = data[4]
    dictionary["telefono"] = data[5]
    dictionary["domicilio"] = data[6]
    dictionary["cargo"] = data[7]
    dictionary["usuario"] = data[8]
    return dictionary

@empleado.post("/empleados", response_model=EmpleadoSchema, status_code=HTTP_201_CREATED)
def guardar(empleado: EmpleadoSchema):
    data = empleado.dict()
    data.pop("id")
    response = Empleado.guardar(data)
    dictionary = {}
    dictionary["id"] = response[0]
    dictionary["ci_o_pasaporte"] = response[1]
    dictionary["nombres"] = response[2]
    dictionary["apellidos"] = response[3]
    dictionary["sexo"] = response[4]
    dictionary["telefono"] = response[5]
    dictionary["domicilio"] = response[6]
    dictionary["cargo"] = response[7]
    dictionary["usuario"] = response[8]
    return dictionary

@empleado.put("/empleados/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, empleado: EmpleadoSchema):
    data = empleado.dict()
    data["id"] = id
    Empleado.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@empleado.delete("/empleados/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar(id: int):
    Empleado.eliminar(id)
    return Response(status_code=HTTP_204_NO_CONTENT)