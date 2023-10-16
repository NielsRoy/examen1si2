from config.database import conn

class Rol:

    __TABLA = "roles"

    @classmethod
    def obtener_todos(cls):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} ")
            return data.fetchall()

    @classmethod
    def obtener_uno(cls, id):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} WHERE id = %s ", (id,))
            return data.fetchone()

    @classmethod
    def guardar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO {cls.__TABLA}(nombre) VALUES(%(nombre)s)", data)
            rol = cls.obtener_el_ultimo()
        conn.commit()
        return rol

    @classmethod
    def actualizar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {cls.__TABLA} SET nombre = %(nombre)s WHERE id = %(id)s", data)
        conn.commit()

    @classmethod
    def eliminar(cls, id):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM {cls.__TABLA} WHERE id = %s ", (id,))
        conn.commit()

    @classmethod
    def obtener_privilegios(cls, id):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT privilegios.* FROM privilegios, roles_tienen_privilegios WHERE rol = %s AND privilegios.id = privilegio", (id,))
            return data.fetchall()

    @classmethod
    def asignar_privilegios(cls, id, privilegios):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM roles_tienen_privilegios WHERE rol = %s ", (id,))
            for privilegio in privilegios:
                print(privilegio)
                cur.execute(f"INSERT INTO roles_tienen_privilegios(privilegio, rol) VALUES(%s, %s)", (privilegio, id))
        conn.commit()

    @classmethod
    def quitar_privilegios(cls, id, privilegios):
        with conn.cursor() as cur:
            for privilegio in privilegios:
                cur.execute(f"DELETE FROM roles_tienen_privilegios WHERE rol = %s AND privilegio = %s ", (id, privilegio))
        conn.commit()

    @classmethod
    def obtener_el_ultimo(cls):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM {cls.__TABLA} ORDER BY id DESC LIMIT 1")
            return data.fetchone()
