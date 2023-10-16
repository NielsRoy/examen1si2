from config.database import conn

class Empleado:

    __TABLA = "empleados"

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
            cur.execute(f"INSERT INTO {cls.__TABLA}(ci_o_pasaporte, nombres, apellidos, sexo, telefono, domicilio, cargo, usuario) VALUES(%(ci_o_pasaporte)s, %(nombres)s, %(apellidos)s, %(sexo)s, %(telefono)s, %(domicilio)s, %(cargo)s, %(usuario)s)", data)
            empleado = cls.obtener_el_ultimo()
        conn.commit()
        return empleado

    @classmethod
    def actualizar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {cls.__TABLA} SET ci_o_pasaporte = %(ci_o_pasaporte)s, nombres = %(nombres)s, apellidos = %(apellidos)s, sexo = %(sexo)s, telefono = %(telefono)s, domicilio = %(domicilio)s, cargo = %(cargo)s, usuario = %(usuario)s WHERE id = %(id)s", data)
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