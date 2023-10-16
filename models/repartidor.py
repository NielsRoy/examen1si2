from config.database import conn

class Repartidor:

    __TABLA = "repartidores"

    @classmethod
    def obtener_todos(cls, pagina, cantidad):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} LIMIT %s OFFSET %s", (cantidad, (pagina - 1) * cantidad))
            return data.fetchall()

    @classmethod
    def obtener_uno(cls, id):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} WHERE id = %s ", (id,))
            return data.fetchone()

    @classmethod
    def guardar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO {cls.__TABLA}(placa, descripcion_del_vehiculo, foto_de_id, foto_de_licencia_de_conducir, foto_de_titulo_de_compra, foto_de_poliza_de_seguro, foto_de_SOAT, empleado) VALUES(%(placa)s, %(descripcion_del_vehiculo)s, %(foto_de_id)s, %(foto_de_licencia_de_conducir)s, %(foto_de_titulo_de_compra)s, %(foto_de_poliza_de_seguro)s, %(foto_de_SOAT)s, %(empleado)s)", data)
            repartidor = cls.obtener_el_ultimo()
        conn.commit()
        return repartidor

    @classmethod
    def actualizar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {cls.__TABLA} SET placa = %(placa)s, descripcion_del_vehiculo = %(descripcion_del_vehiculo)s, empleado = %(empleado)s WHERE id = %(id)s", data)
        conn.commit()

    @classmethod
    def eliminar(cls, id):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM {cls.__TABLA} WHERE id = %s ", (id,))
        conn.commit()

    @classmethod
    def obtener_el_ultimo(cls):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} ORDER BY id DESC LIMIT 1")
            return data.fetchone()

    @classmethod
    def actualizar_foto(cls, id, nombre, campo):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {cls.__TABLA} SET {campo} = %s WHERE id = %s ", (nombre, id))
        conn.commit()

    @classmethod
    def obtener_foto(cls, id, campo):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT {campo} FROM {cls.__TABLA} WHERE id = %s ", (id,))
            return data.fetchone()
        
    @classmethod
    def obtener_fotos_del_vehiculo(cls, repartidor):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT path FROM fotos_del_vehiculo WHERE repartidor = %s ", (repartidor,))
            return data.fetchall()

    @classmethod
    def subir_foto_del_vehiculo(cls, repartidor, path):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO fotos_del_vehiculo(repartidor, path) VALUES(%s, %s)", (repartidor, path))
        conn.commit()

    @classmethod
    def eliminar_foto_del_vehiculo(cls, repartidor, path):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM fotos_del_vehiculo WHERE repartidor = %s AND path =%s ", (repartidor, path))
        conn.commit()

    @classmethod
    def obtener_foto_del_vehiculo(cls, repartidor, path):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT path FROM fotos_del_vehiculo WHERE repartidor = %s AND path =%s ", (repartidor, path))
            return data.fetchone()