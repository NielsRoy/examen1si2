from config.database import conn

class NotaDeVenta:

    __TABLA = "notas_de_venta"

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
            cur.execute(f"INSERT INTO {cls.__TABLA}(fecha, hora, monto, descuento, monto_final, cliente) VALUES(%(fecha)s, %(hora)s, %(monto)s, %(descuento)s, %(monto_final)s, %(cliente)s)", data)
            pedido = cls.obtener_el_ultimo()
        conn.commit()
        return pedido

    @classmethod
    def actualizar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {cls.__TABLA} SET fecha = %(fecha)s, hora = %(hora)s, monto = %(monto)s, descuento = %(descuento)s, monto_final = %(monto_final)s, cliente = %(cliente)s WHERE nro = %(nro)s", data)
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
            data = cur.execute(f"SELECT * FROM detalles_de_venta WHERE nota_de_venta = %s ", (nro,))
            return data.fetchall()
        
    @classmethod
    def agregar_detalle(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO detalles_de_venta(nota_de_venta, producto, cantidad, monto, descuento) VALUES(%(nota_de_venta)s, %(producto)s, %(cantidad)s, %(monto)s, %(descuento)s)", data)
        conn.commit()

    @classmethod
    def actualizar_detalle(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE detalles_de_venta SET cantidad = %(cantidad)s, monto = %(monto)s, descuento = %(descuento)s WHERE nota_de_venta = %(nota_de_venta)s AND producto = %(producto)s", data)
        conn.commit()

    @classmethod
    def eliminar_detalle(cls, nota_de_venta, producto):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM detalles_de_venta WHERE nota_de_venta = %s AND producto = %s ", (nota_de_venta, producto))
        conn.commit()