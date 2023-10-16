from fastapi import APIRouter, Response
from models.pedido import Pedido
from schemas.pedido import PedidoSchema
from schemas.detalle_del_pedido import DetalleDelPedidoSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

pedido = APIRouter()

@pedido.get("/pedidos", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Pedido.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["nro"] = data[0]
        dictionary["fecha"] = data[1]
        dictionary["hora"] = data[2]
        dictionary["cliente"] = data[3]
        dictionary["repartidor"] = data[4]
        dictionary["direccion_de_entrega"] = data[5]
        dictionary["completado"] = data[6]
        items.append(dictionary)
    return items

@pedido.get("/pedidos/{nro}", status_code=HTTP_200_OK)
def mostrar_uno(nro: int):
    data = Pedido.obtener_uno(nro)
    dictionary = {}
    dictionary["nro"] = data[0]
    dictionary["fecha"] = data[1]
    dictionary["hora"] = data[2]
    dictionary["cliente"] = data[3]
    dictionary["repartidor"] = data[4]
    dictionary["direccion_de_entrega"] = data[5]
    dictionary["completado"] = data[6]
    return dictionary

@pedido.post("/pedidos", response_model=PedidoSchema, status_code=HTTP_201_CREATED)
def guardar(pedido: PedidoSchema):
    data = pedido.dict()
    data.pop("nro")
    response = Pedido.guardar(data)
    dictionary = {}
    dictionary["nro"] = response[0]
    dictionary["fecha"] = response[1]
    dictionary["hora"] = response[2]
    dictionary["cliente"] = response[3]
    dictionary["repartidor"] = response[4]
    dictionary["direccion_de_entrega"] = response[5]
    dictionary["completado"] = response[6]
    return dictionary

@pedido.put("/pedidos/{nro}", status_code=HTTP_204_NO_CONTENT)
def actualizar(nro: int, pedido: PedidoSchema):
    data = pedido.dict()
    data["nro"] = nro
    Pedido.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@pedido.delete("/pedidos/{nro}", status_code=HTTP_204_NO_CONTENT)
def eliminar(nro: int):
    Pedido.eliminar(nro)
    return Response(status_code=HTTP_204_NO_CONTENT)

@pedido.get("/pedidos/{nro}/detalles", status_code=HTTP_200_OK)
def mostrar_detalles(nro: int):
    items = []
    for data in Pedido.obtener_detalles(nro):
        dictionary = {}
        dictionary["producto"] = data[1]
        dictionary["cantidad"] = data[2]
        items.append(dictionary)
    return items

@pedido.post("/pedidos/{nro}/detalles")
def agregar_detalles(nro: int, detalle: DetalleDelPedidoSchema):
    data = detalle.dict()
    data["pedido"] = nro
    Pedido.agregar_detalle(data)
    return Response(status_code=HTTP_201_CREATED)

@pedido.put("/pedidos/{nro}/detalles/{producto}")
def actualizar_detalle(nro: int, producto: str, detalle: DetalleDelPedidoSchema):
    data = detalle.dict()
    data["pedido"] = nro
    data["producto"] = producto
    Pedido.actualizar_detalle(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@pedido.delete("/pedidos/{nro}/detalles/{producto}")
def quitar_detalle(nro: int, producto: str):
    Pedido.eliminar_detalle(nro, producto)
    return Response(status_code=HTTP_204_NO_CONTENT)

