from fastapi import APIRouter, Response
from models.nota_de_venta import NotaDeVenta
from schemas.nota_de_venta import NotaDeVentaSchema
from schemas.detalle_de_venta import DetalleDeVentaSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

nota_de_venta = APIRouter()

@nota_de_venta.get("/notas-de-venta", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in NotaDeVenta.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["nro"] = data[0]
        dictionary["fecha"] = data[1]
        dictionary["hora"] = data[2]
        dictionary["monto"] = data[3]
        dictionary["descuento"] = data[4]
        dictionary["monto_final"] = data[5]
        dictionary["cliente"] = data[6]
        items.append(dictionary)
    return items

@nota_de_venta.get("/notas-de-venta/{nro}", status_code=HTTP_200_OK)
def mostrar_uno(nro: int):
    data = NotaDeVenta.obtener_uno(nro)
    dictionary = {}
    dictionary["nro"] = data[0]
    dictionary["fecha"] = data[1]
    dictionary["hora"] = data[2]
    dictionary["monto"] = data[3]
    dictionary["descuento"] = data[4]
    dictionary["monto_final"] = data[5]
    dictionary["cliente"] = data[6]
    return dictionary

@nota_de_venta.post("/notas-de-venta", response_model=NotaDeVentaSchema, status_code=HTTP_201_CREATED)
def guardar(nota_de_venta: NotaDeVentaSchema):
    data = nota_de_venta.dict()
    data.pop("nro")
    response = NotaDeVenta.guardar(data)
    dictionary = {}
    dictionary["nro"] = response[0]
    dictionary["fecha"] = response[1]
    dictionary["hora"] = response[2]
    dictionary["monto"] = response[3]
    dictionary["descuento"] = response[4]
    dictionary["monto_final"] = response[5]
    dictionary["cliente"] = response[6]
    return dictionary

@nota_de_venta.put("/notas-de-venta/{nro}", status_code=HTTP_204_NO_CONTENT)
def actualizar(nro: int, nota_de_venta: NotaDeVentaSchema):
    data = nota_de_venta.dict()
    data["nro"] = nro
    NotaDeVenta.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@nota_de_venta.delete("/notas-de-venta/{nro}", status_code=HTTP_204_NO_CONTENT)
def eliminar(nro: int):
    NotaDeVenta.eliminar(nro)
    return Response(status_code=HTTP_204_NO_CONTENT)

@nota_de_venta.get("/notas-de-venta/{nro}/detalles", status_code=HTTP_200_OK)
def mostrar_detalles(nro: int):
    items = []
    for data in NotaDeVenta.obtener_detalles(nro):
        dictionary = {}
        dictionary["producto"] = data[1]
        dictionary["cantidad"] = data[2]
        dictionary["monto"] = data[3]
        dictionary["descuento"] = data[4]
        items.append(dictionary)
    return items

@nota_de_venta.post("/notas-de-venta/{nro}/detalles", response_model=DetalleDeVentaSchema, status_code=HTTP_201_CREATED)
def agregar_detalle(nro: int, detalle: DetalleDeVentaSchema):
    data = detalle.dict()
    data["nota_de_venta"] = nro
    NotaDeVenta.agregar_detalle(data)
    return Response(status_code=HTTP_201_CREATED)
    
@nota_de_venta.put("/notas-de-venta/{nro}/detalles/{producto}", status_code=HTTP_204_NO_CONTENT)
def actualizar_detalle(nro: int, producto: str, detalle: DetalleDeVentaSchema):
    data = detalle.dict()
    data["nota_de_venta"] = nro
    data["producto"] = producto
    NotaDeVenta.actualizar_detalle(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@nota_de_venta.delete("/notas-de-venta/{nro}/detalles/{producto}", status_code=HTTP_204_NO_CONTENT)
def eliminar_detalle(nro: int, producto: str):
    NotaDeVenta.eliminar_detalle(nro, producto)
    return Response(status_code=HTTP_204_NO_CONTENT)