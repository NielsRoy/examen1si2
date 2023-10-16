from fastapi import APIRouter, Response, File, UploadFile
from models.usuario import Usuario
from schemas.usuario import UsuarioSchema
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT


# para subir imagenes
# pip install python-multipart
import uuid
import os
from fastapi.responses import FileResponse

# pip install cryptography
from cryptography.fernet import Fernet # TODO: Revisar si sirve para contraseñas

IMAGEDIR = "images/usuarios/"

usuario = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

@usuario.get("/usuarios", status_code=HTTP_200_OK)
def mostrar_todos(pagina: int = 1, cantidad: int = 10):
    items = []
    for data in Usuario.obtener_todos(pagina, cantidad):
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["email"] = data[1]
        dictionary["clave"] = data[2]
        dictionary["foto"] = data[3]
        dictionary["rol"] = data[4]
        items.append(dictionary)
    return items

@usuario.get("/usuarios/{id}", status_code=HTTP_200_OK)
def mostrar_uno(id: int):
    data = Usuario.obtener_uno(id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["email"] = data[1]
    dictionary["clave"] = data[2]
    dictionary["foto"] = data[3]
    dictionary["rol"] = data[4]
    return dictionary

@usuario.post("/usuarios", response_model=UsuarioSchema, status_code=HTTP_201_CREATED)
def guardar(usuario: UsuarioSchema):
    data = usuario.dict()
    data["clave"] = f.encrypt(usuario.clave.encode("utf-8"))
    data.pop("id")
    response = Usuario.guardar(data)
    dictionary = {}
    dictionary["id"] = response[0]
    dictionary["email"] = response[1]
    dictionary["clave"] = response[2]
    dictionary["foto"] = response[3]
    dictionary["rol"] = response[4]
    return dictionary

@usuario.put("/usuarios/{id}", status_code=HTTP_204_NO_CONTENT)
def actualizar(id: int, usuario: UsuarioSchema):
    data = usuario.dict()
    data.pop("foto")
    data["clave"] = f.encrypt(usuario.clave.encode("utf-8"))
    data["id"] = id
    Usuario.actualizar(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@usuario.delete("/usuarios/{id}", status_code=HTTP_204_NO_CONTENT)
def eliminar(id: int):
    eliminar_foto(id)
    Usuario.eliminar(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

# solo jpg, png, jpeg
@usuario.post("/usuarios/{id}/foto", status_code=HTTP_204_NO_CONTENT)
async def actualizar_foto(id: int, foto: UploadFile = File(...)):
    eliminar_foto(id)
    
    extension = foto.filename.split(".")[-1]
    nombre = f"{uuid.uuid4()}.{extension}"
    foto.filename = nombre
    content = await foto.read()

    with open(f"{IMAGEDIR}{foto.filename}", "wb") as buffer:
        buffer.write(content)
        # buffer.write(foto.file.read())

    Usuario.actualizar_foto(id, nombre)
    return Response(status_code=HTTP_204_NO_CONTENT)

@usuario.get("/usuarios/{id}/foto")
async def mostrar_foto(id: int):
    if Usuario.obtener_foto(id)[0] is not None:
        file = f"{IMAGEDIR}{Usuario.obtener_foto(id)[0]}"
        return FileResponse(file)

def eliminar_foto(id):
    foto = Usuario.obtener_foto(id)[0] 
    if foto is not None:
        os.remove(f"{IMAGEDIR}{foto}")