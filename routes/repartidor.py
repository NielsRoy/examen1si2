from fastapi import APIRouter, Response, File, UploadFile
from models.repartidor import Repartidor
from schemas.repartidor import RepartidorSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from fastapi.responses import JSONResponse 

import uuid
import os
from fastapi.responses import FileResponse

from typing import List

IMAGEDIR = "images/repartidores/"

repartidor = APIRouter()

@repartidor.get("/repartidores", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Repartidor.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["placa"] = data[1]
        dictionary["descripcion_del_vehiculo"] = data[2]
        dictionary["foto_de_id"] = data[3]
        dictionary["foto_de_licencia_de_conducir"] = data[4]
        dictionary["foto_de_titulo_de_compra"] = data[5]
        dictionary["foto_de_poliza_de_seguro"] = data[6]
        dictionary["foto_de_SOAT"] = data[7]
        dictionary["empleado"] = data[8]
        items.append(dictionary)
    return items

@repartidor.get("/repartidores/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Repartidor.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["placa"] = data[1]
    dictionary["descripcion_del_vehiculo"] = data[2]
    dictionary["foto_de_id"] = data[3]
    dictionary["foto_de_licencia_de_conducir"] = data[4]
    dictionary["foto_de_titulo_de_compra"] = data[5]
    dictionary["foto_de_poliza_de_seguro"] = data[6]
    dictionary["foto_de_SOAT"] = data[7]
    dictionary["empleado"] = data[8]
    return dictionary

@repartidor.post("/repartidores", response_model=RepartidorSchema, status_code=HTTP_201_CREATED)
def guardar(repartidor: RepartidorSchema):
    data = repartidor.dict()
    data.pop("id")
    response = Repartidor.guardar(data)
    dictionary = {}
    dictionary["id"] = response[0]
    dictionary["placa"] = response[1]
    dictionary["descripcion_del_vehiculo"] = response[2]
    dictionary["foto_de_id"] = response[3]
    dictionary["foto_de_licencia_de_conducir"] = response[4]
    dictionary["foto_de_titulo_de_compra"] = response[5]
    dictionary["foto_de_poliza_de_seguro"] = response[6]
    dictionary["foto_de_SOAT"] = response[7]
    dictionary["empleado"] = response[8]
    return dictionary

@repartidor.put("/repartidores/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, repartidor: RepartidorSchema):
    data = repartidor.dict()
    data.pop("foto_de_id")
    data.pop("foto_de_licencia_de_conducir")
    data.pop("foto_de_titulo_de_compra")
    data.pop("foto_de_poliza_de_seguro")
    data.pop("foto_de_SOAT")
    data["id"] = id
    Repartidor.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@repartidor.delete("/repartidores/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar(id: int):
    eliminar_foto(id, "foto_de_id")
    eliminar_foto(id, "foto_de_licencia_de_conducir")
    eliminar_foto(id, "foto_de_titulo_de_compra")
    eliminar_foto(id, "foto_de_poliza_de_seguro")
    eliminar_foto(id, "foto_de_SOAT")
    Repartidor.eliminar(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

# solo jpg, png, jpeg
@repartidor.post("/repartidores/{id}/foto_de_id", status_code=HTTP_204_NO_CONTENT)
async def actualizar_foto_de_id(id: int, foto_de_id: UploadFile = File(...)):
    eliminar_foto(id, "foto_de_id")
    
    extension = foto_de_id.filename.split(".")[-1]
    nombre = f"{uuid.uuid4()}.{extension}"
    foto_de_id.filename = nombre
    content = await foto_de_id.read()

    with open(f"{IMAGEDIR}{foto_de_id.filename}", "wb") as buffer:
        buffer.write(content)
        # buffer.write(foto_de_id.file.read())

    Repartidor.actualizar_foto(id, nombre, "foto_de_id")
    return Response(status_code=HTTP_204_NO_CONTENT)

@repartidor.post("/repartidores/{id}/foto_de_licencia_de_conducir", status_code=HTTP_204_NO_CONTENT)
async def actualizar_foto_de_licencia_de_conducir(id: int, foto_de_licencia_de_conducir: UploadFile = File(...)):
    eliminar_foto(id, "foto_de_licencia_de_conducir")
    
    extension = foto_de_licencia_de_conducir.filename.split(".")[-1]
    nombre = f"{uuid.uuid4()}.{extension}"
    foto_de_licencia_de_conducir.filename = nombre
    content = await foto_de_licencia_de_conducir.read()

    with open(f"{IMAGEDIR}{foto_de_licencia_de_conducir.filename}", "wb") as buffer:
        buffer.write(content)
        # buffer.write(foto_de_id.file.read())

    Repartidor.actualizar_foto(id, nombre, "foto_de_licencia_de_conducir")
    return Response(status_code=HTTP_204_NO_CONTENT)

@repartidor.post("/repartidores/{id}/foto_de_titulo_de_compra", status_code=HTTP_204_NO_CONTENT)
async def actualizar_foto_de_titulo_de_compra(id: int, foto_de_titulo_de_compra: UploadFile = File(...)):
    eliminar_foto(id, "foto_de_titulo_de_compra")
    
    extension = foto_de_titulo_de_compra.filename.split(".")[-1]
    nombre = f"{uuid.uuid4()}.{extension}"
    foto_de_titulo_de_compra.filename = nombre
    content = await foto_de_titulo_de_compra.read()

    with open(f"{IMAGEDIR}{foto_de_titulo_de_compra.filename}", "wb") as buffer:
        buffer.write(content)
        # buffer.write(foto_de_id.file.read())

    Repartidor.actualizar_foto(id, nombre, "foto_de_titulo_de_compra")
    return Response(status_code=HTTP_204_NO_CONTENT)

@repartidor.post("/repartidores/{id}/foto_de_poliza_de_seguro", status_code=HTTP_204_NO_CONTENT)
async def actualizar_foto_de_poliza_de_seguro(id: int, foto_de_poliza_de_seguro: UploadFile = File(...)):
    eliminar_foto(id, "foto_de_poliza_de_seguro")
    
    extension = foto_de_poliza_de_seguro.filename.split(".")[-1]
    nombre = f"{uuid.uuid4()}.{extension}"
    foto_de_poliza_de_seguro.filename = nombre
    content = await foto_de_poliza_de_seguro.read()

    with open(f"{IMAGEDIR}{foto_de_poliza_de_seguro.filename}", "wb") as buffer:
        buffer.write(content)
        # buffer.write(foto_de_id.file.read())

    Repartidor.actualizar_foto(id, nombre, "foto_de_poliza_de_seguro")
    return Response(status_code=HTTP_204_NO_CONTENT)

@repartidor.post("/repartidores/{id}/foto_de_SOAT", status_code=HTTP_204_NO_CONTENT)
async def actualizar_foto_de_SOAT(id: int, foto_de_SOAT: UploadFile = File(...)):
    eliminar_foto(id, "foto_de_SOAT")
    
    extension = foto_de_SOAT.filename.split(".")[-1]
    nombre = f"{uuid.uuid4()}.{extension}"
    foto_de_SOAT.filename = nombre
    content = await foto_de_SOAT.read()

    with open(f"{IMAGEDIR}{foto_de_SOAT.filename}", "wb") as buffer:
        buffer.write(content)
        # buffer.write(foto_de_id.file.read())

    Repartidor.actualizar_foto(id, nombre, "foto_de_SOAT")
    return Response(status_code=HTTP_204_NO_CONTENT)


@repartidor.get("/repartidores/{id}/foto_de_id")
async def mostrar_foto_de_id(id: int):
    return mostrar_foto(id, "foto_de_id")

@repartidor.get("/repartidores/{id}/foto_de_licencia_de_conducir")
async def mostrar_foto_de_licencia_de_conducir(id: int):
    return mostrar_foto(id, "foto_de_licencia_de_conducir")

@repartidor.get("/repartidores/{id}/foto_de_titulo_de_compra")
async def mostrar_foto_de_titulo_de_compra(id: int):
    return mostrar_foto(id, "foto_de_titulo_de_compra")

@repartidor.get("/repartidores/{id}/foto_de_poliza_de_seguro")
async def mostrar_foto_de_poliza_de_seguro(id: int):
    return mostrar_foto(id, "foto_de_poliza_de_seguro")

@repartidor.get("/repartidores/{id}/foto_de_SOAT")
async def mostrar_foto_de_SOAT(id: int):
    return mostrar_foto(id, "foto_de_SOAT")

@repartidor.get("/repartidores/{id}/fotos_del_vehiculo", status_code=HTTP_200_OK)
def mostrar_fotos_del_vehiculo(id: int):
    items = []
    for foto in Repartidor.obtener_fotos_del_vehiculo(id):
        file = f"{foto[0]}"
        items.append(file)
    return items

@repartidor.post("/repartidores/{id}/fotos_del_vehiculo", status_code=HTTP_204_NO_CONTENT)
async def subir_fotos_del_vehiculo(id: int, fotos: List[UploadFile] = File(...)):
    try:
        for foto in fotos:
            extension = foto.filename.split(".")[-1]
            nombre = f"{uuid.uuid4()}.{extension}"
            with open(f"{IMAGEDIR}{nombre}", "wb") as buffer:
                content = await foto.read()
                buffer.write(content)
                buffer.close()
            Repartidor.subir_foto_del_vehiculo(id, nombre)
        return JSONResponse(status_code=200, content={"mensaje": "Fotos subidas correctamente"})
    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"mensaje": "No se pudo subir las fotos"})
    
@repartidor.delete("/repartidores/{id}/fotos_del_vehiculo/{foto}", status_code=HTTP_200_OK)
def eliminar_foto_del_vehiculo(id: int, foto: str):
    try:
        Repartidor.eliminar_foto_del_vehiculo(id, foto)
        os.remove(f"{IMAGEDIR}{foto}")
        return JSONResponse(status_code=200, content={"mensaje": "Foto eliminada correctamente"})
    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"mensaje": "No se pudo eliminar la foto"})

def mostrar_foto(id: int, campo):
    foto = Repartidor.obtener_foto(id, campo)[0] 
    if foto is not None:
        file = f"{IMAGEDIR}{foto}"
        return FileResponse(file)

def eliminar_foto(id, campo):
    foto = Repartidor.obtener_foto(id, campo)[0] 
    #verificar si la foto existe en el sistema operativo

    if foto is not None and os.path.exists(f"{IMAGEDIR}{foto}") :
        os.remove(f"{IMAGEDIR}{foto}")

@repartidor.get("/repartidores/{id}/fotos_del_vehiculo/{foto}", status_code=HTTP_200_OK)
async def mostrar_foto_del_vehiculo(id: int, foto: str):
    foto = Repartidor.obtener_foto_del_vehiculo(id, foto)[0]
    if foto is not None:
        file = f"{IMAGEDIR}{foto}"
        return FileResponse(file)

        