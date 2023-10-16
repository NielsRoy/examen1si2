from config.database import conn

class Producto:

    __TABLA = "productos"

    @classmethod
    def obtener_todos(cls, pagina, cantidad):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} LIMIT %s OFFSET %s", (cantidad, (pagina - 1) * cantidad))
            return data.fetchall()

    @classmethod
    def obtener_uno(cls, codigo):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} WHERE codigo = %s ", (codigo,))
            return data.fetchone()

    @classmethod
    def guardar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO {cls.__TABLA}(codigo, descripcion, precio, descuento, material, marca) VALUES(%(codigo)s, %(descripcion)s, %(precio)s, %(descuento)s, %(material)s, %(marca)s)", data)
        conn.commit()

    @classmethod
    def actualizar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {cls.__TABLA} SET codigo = %(codigo)s, descripcion = %(descripcion)s, precio = %(precio)s, descuento = %(descuento)s, material = %(material)s, marca = %(marca)s WHERE codigo = %(codigo_anterior)s", data)
        conn.commit()

    @classmethod
    def eliminar(cls, codigo):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM {cls.__TABLA} WHERE codigo = %s ", (codigo,))
            cur.execute(f"DELETE FROM fotos_del_producto WHERE producto = %s ", (codigo,)) #TODO: Revisar si es innecesario
        conn.commit()

    @classmethod
    def obtener_fotos(cls, codigo):
        with conn.cursor() as cur:
            cur.execute(f"SELECT path FROM fotos_del_producto WHERE producto = %s ", (codigo,))
            return cur.fetchall()

    @classmethod
    def subir_foto(cls, codigo, nombre):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO fotos_del_producto(producto, path) VALUES(%s, %s)", (codigo, nombre))
        conn.commit()

    @classmethod
    def eliminar_foto(cls, codigo, foto):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM fotos_del_producto WHERE producto = %s AND path = %s", (codigo, foto))
        conn.commit()

    @classmethod
    def obtener_tallas(cls, codigo):
        with conn.cursor() as cur:
            cur.execute(f"SELECT distinct(talla) FROM productos_tienen_tallas WHERE producto = %s ", (codigo,))
            return cur.fetchall()

    @classmethod
    def eliminar_talla(cls, codigo, talla):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM productos_tienen_tallas WHERE producto = %s AND talla = %s AND cantidad = 0", (codigo, talla))
        conn.commit()

    @classmethod
    def obtener_stock(cls, codigo):
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM productos_tienen_tallas WHERE producto = %s ", (codigo,))
            return cur.fetchall()

    @classmethod
    def actualizar_stock(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM productos_tienen_tallas WHERE producto = %(codigo)s AND talla = %(talla)s AND sucursal = %(sucursal)s", data)
            existe = cur.fetchone()

            if (existe is None):
                cur.execute(f"INSERT INTO productos_tienen_tallas(producto, talla, sucursal, cantidad) VALUES(%(codigo)s, %(talla)s, %(sucursal)s, %(cantidad)s)", data)
            else:
                cur.execute(f"UPDATE productos_tienen_tallas SET cantidad = %(cantidad)s WHERE producto = %(codigo)s AND talla = %(talla)s AND sucursal = %(sucursal)s", data)
        conn.commit()

    @classmethod
    def obtener_categorias(cls, codigo):
        with conn.cursor() as cur:
            cur.execute(f"SELECT categoria FROM productos_tienen_categorias WHERE producto = %s ", (codigo,))
            return cur.fetchall()

    @classmethod
    def agregar_categoria(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO productos_tienen_categorias(producto, categoria) VALUES(%(codigo)s, %(id)s)", data)
        conn.commit()

    @classmethod
    def quitar_categoria(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM productos_tienen_categorias WHERE producto = %(codigo)s AND categoria = %(id)s", data)
        conn.commit()