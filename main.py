from fastapi import FastAPI
from routes.usuario import usuario
from routes.rol import rol
from routes.privilegio import privilegio
from routes.marca import marca
from routes.talla import talla
from routes.producto import producto
from routes.sucursal import sucursal
from routes.categoria import categoria
from routes.cliente import cliente
from routes.cargo import cargo
from routes.empleado import empleado
from routes.repartidor import repartidor
from routes.pedido import pedido
from routes.nota_de_venta import nota_de_venta

# autopep8 => sirve para formatear el codigo mientras trabajamos en el

app = FastAPI()


# ecommerce-env\Scripts\activate.bat => Para activar el entorno virtual

# uvicorn main:app --reload  => Para leventar el servidor uvicorn
# main => Es el nombre del archivo donde esta la instancia de FastAPI
# app => Es la instancia de FastAPI
# --reload => Para que se reinicie el servidor cada vez que se haga un cambio
# NOTA: no usar --reload en produccion


app.include_router(usuario)
app.include_router(rol)
app.include_router(privilegio)
app.include_router(marca)
app.include_router(talla)
app.include_router(producto)
app.include_router(sucursal)
app.include_router(categoria)
app.include_router(cliente)
app.include_router(cargo)
app.include_router(empleado)
app.include_router(repartidor)
app.include_router(pedido)
app.include_router(nota_de_venta)