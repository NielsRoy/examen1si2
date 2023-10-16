from config.database import conn

class Usuario:

    __TABLA = "usuarios"

    @classmethod
    def obtener_todos(cls, pagina, cantidad):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} LIMIT %s OFFSET %s", (cantidad, (pagina - 1) * cantidad))
            return data.fetchall()
        # with conn.cursor() as cur:
        #     data = cur.execute(f"SELECT * FROM {cls.__TABLA} ")
        #     return data.fetchall()

    @classmethod
    def obtener_uno(cls, id):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} WHERE id = %s ", (id,))
            return data.fetchone()

    @classmethod
    def guardar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO {cls.__TABLA}(email, clave, foto, rol) VALUES(%(email)s, %(clave)s, %(foto)s, %(rol)s)", data)
            usuario = cls.obtener_el_ultimo()
        conn.commit()
        return usuario

    @classmethod
    def actualizar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {cls.__TABLA} SET email = %(email)s, clave = %(clave)s, rol = %(rol)s WHERE id = %(id)s", data)
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
    def actualizar_foto(cls, id, nombre):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {cls.__TABLA} SET foto = %s WHERE id = %s ", (nombre, id))
        conn.commit()

    @classmethod
    def obtener_foto(cls, id):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT foto FROM {cls.__TABLA} WHERE id = %s ", (id,))
            return data.fetchone()