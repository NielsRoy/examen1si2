from fastapi import APIRouter, Response, File, UploadFile
from models.producto import Producto
from schemas.producto import ProductoSchema
from schemas.stock import StockSchema
from schemas.categoria import CategoriaSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from fastapi.responses import JSONResponse 

import uuid
import os
from fastapi.responses import FileResponse

from typing import List

IMAGEDIR = "images/productos/"

producto = APIRouter()

@producto.get("/productos", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Producto.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["codigo"] = data[0]
        dictionary["descripcion"] = data[1]
        dictionary["precio"] = data[2]
        dictionary["descuento"] = data[3]
        dictionary["material"] = data[4]
        dictionary["marca"] = data[5]
        items.append(dictionary)
    return items

@producto.get("/productos/{codigo}", status_code=HTTP_200_OK)
def mostrar_uno(codigo: str):
    data = Producto.obtener_uno(codigo)
    dictionary = {}
    dictionary["codigo"] = data[0]
    dictionary["descripcion"] = data[1]
    dictionary["precio"] = data[2]
    dictionary["descuento"] = data[3]
    dictionary["material"] = data[4]
    dictionary["marca"] = data[5]
    return dictionary

@producto.post("/productos", response_model=ProductoSchema, status_code=HTTP_201_CREATED)
def guardar(producto: ProductoSchema):
    data = producto.dict()
    Producto.guardar(data)
    return Response(status_code=HTTP_201_CREATED)

@producto.put("/productos/{codigo}", status_code=HTTP_204_NO_CONTENT)
def actualizar(codigo: str, producto: ProductoSchema):
    data = producto.dict()
    data["codigo_anterior"] = codigo
    Producto.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@producto.delete("/productos/{codigo}", status_code=HTTP_204_NO_CONTENT)
def eliminar(codigo: str):
    fotos = Producto.obtener_fotos(codigo)
    Producto.eliminar(codigo)
    for foto in fotos:
        os.remove(f"{IMAGEDIR}{foto[0]}")
    return Response(status_code=HTTP_204_NO_CONTENT)

@producto.get("/productos/{codigo}/fotos", status_code=HTTP_200_OK)
def mostrar_fotos(codigo: str):
    fotos = Producto.obtener_fotos(codigo)
    if fotos is None:
        return JSONResponse(status_code=404, content={"mensaje": "No se encontraron fotos"})
    
    items = []
    for foto in fotos:
        file = f"{IMAGEDIR}{foto[0]}"
        items.append(file)
        # items.append(FileResponse(file))
    return items

@producto.get("/productos/{codigo}/fotos/{foto}", status_code=HTTP_200_OK)
def mostrar_foto(codigo: str, foto: str):
    file = f"{IMAGEDIR}{foto}"
    return FileResponse(file)    

@producto.post("/productos/{codigo}/fotos", status_code=HTTP_201_CREATED)
async def subir_fotos(codigo: str, fotos: List[UploadFile] = File(...)):
    try:
        for foto in fotos:
            extension = foto.filename.split(".")[-1]
            nombre = f"{uuid.uuid4()}.{extension}"
            with open(f"{IMAGEDIR}{nombre}", "wb") as buffer:
                content = await foto.read()
                buffer.write(content)
                buffer.close()
            Producto.subir_foto(codigo, nombre)
        return JSONResponse(status_code=200, content={"mensaje": "Fotos subidas correctamente"})
    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"mensaje": "No se pudo subir las fotos"})
    
@producto.delete("/productos/{codigo}/fotos/{foto}", status_code=HTTP_200_OK)    
def eliminar_foto(codigo: str, foto: str):
    try:
        Producto.eliminar_foto(codigo, foto)
        os.remove(f"{IMAGEDIR}{foto}")
        return JSONResponse(status_code=200, content={"mensaje": "Foto eliminada correctamente"})
    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"mensaje": "No se pudo eliminar la foto"})

@producto.get("/productos/{codigo}/tallas", status_code=HTTP_200_OK)
def mostrar_tallas(codigo: str):
    items = []
    for talla in Producto.obtener_tallas(codigo):
        items.append(talla[0])
    return items

@producto.delete("/productos/{codigo}/tallas/{talla}", status_code=HTTP_204_NO_CONTENT)
def eliminar_talla(codigo: str, talla: int):
    Producto.eliminar_talla(codigo, talla)
    return Response(status_code=HTTP_204_NO_CONTENT)

@producto.get("/productos/{codigo}/stock", status_code=HTTP_200_OK)
def mostrar_stock(codigo: str):
    items = []
    for stock in Producto.obtener_stock(codigo):
        dictionary = {}
        dictionary["talla"] = stock[1]
        dictionary["sucursal"] = stock[2]
        dictionary["cantidad"] = stock[3]
        items.append(dictionary)
    return items

@producto.post("/productos/{codigo}/stock")
def actualizar_stock(codigo: str, stock: StockSchema):
    data = stock.dict()
    data["codigo"] = codigo
    Producto.actualizar_stock(data)
    return JSONResponse(status_code=200, content={"mensaje": "Stock actualizado correctamente"})


@producto.get("/productos/{codigo}/categorias", status_code=HTTP_200_OK)
def mostrar_categorias(codigo: str):
    items = []
    for categoria in Producto.obtener_categorias(codigo):
        items.append(categoria[0])
    return items

@producto.post("/productos/{codigo}/categorias")
def agregar_categoria(codigo: str, categoria: CategoriaSchema):
    data = categoria.dict()
    data.pop("nombre")
    data["codigo"] = codigo
    Producto.agregar_categoria(data)
    return JSONResponse(status_code=200, content={"mensaje": "Categoria agregada correctamente"})

@producto.delete("/productos/{codigo}/categorias")
def quitar_categoria(codigo: str, categoria: CategoriaSchema):
    data = categoria.dict()
    data.pop("nombre")
    data["codigo"] = codigo
    Producto.quitar_categoria(data)
    return JSONResponse(status_code=200, content={"mensaje": "Categoria quitada correctamente"})