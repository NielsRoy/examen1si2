from config.database import conn

class Pedido:

    __TABLA = "pedidos"

    @classmethod
    def obtener_todos(cls, pagina, cantidad):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} LIMIT %s OFFSET %s", (cantidad, (pagina - 1) * cantidad))
            return data.fetchall()

    @classmethod
    def obtener_uno(cls, nro):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} WHERE nro = %s ", (nro,))
            return data.fetchone()

    @classmethod
    def guardar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO {cls.__TABLA}(fecha, hora, cliente, repartidor, direccion_de_entrega, completado) VALUES(%(fecha)s, %(hora)s, %(cliente)s, %(repartidor)s, %(direccion_de_entrega)s, %(completado)s)", data)
            pedido = cls.obtener_el_ultimo()
        conn.commit()
        return pedido

    @classmethod
    def actualizar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {cls.__TABLA} SET fecha = %(fecha)s, hora = %(hora)s, cliente = %(cliente)s, repartidor = %(repartidor)s, direccion_de_entrega = %(direccion_de_entrega)s, completado = %(completado)s WHERE nro = %(nro)s", data)
        conn.commit()

    @classmethod
    def eliminar(cls, nro):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM {cls.__TABLA} WHERE nro = %s ", (nro,))
        conn.commit()

    @classmethod
    def obtener_el_ultimo(cls):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} ORDER BY nro DESC LIMIT 1")
            return data.fetchone()
        
    @classmethod
    def obtener_detalles(cls, nro):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM detalles_del_pedido WHERE pedido = %s", (nro,))
            return data.fetchall()
        
    @classmethod
    def agregar_detalle(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO detalles_del_pedido(pedido, producto, cantidad) VALUES(%(pedido)s, %(producto)s, %(cantidad)s)", data)
        conn.commit()

    @classmethod
    def actualizar_detalle(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE detalles_del_pedido SET cantidad = %(cantidad)s WHERE pedido = %(pedido)s AND producto = %(producto)s", data)
        conn.commit()

    @classmethod
    def eliminar_detalle(cls, pedido, producto):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM detalles_del_pedido WHERE pedido = %s AND producto = %s", (pedido, producto))
        conn.commit()
        





