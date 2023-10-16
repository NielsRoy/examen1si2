from config.database import conn

class Cliente:

    __TABLA = "clientes"

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
            cur.execute(f"INSERT INTO {cls.__TABLA}(nombres, apellidos, telefono, sexo, usuario) VALUES(%(nombres)s, %(apellidos)s, %(telefono)s, %(sexo)s, %(usuario)s)", data)
            cliente = cls.obtener_el_ultimo()
        conn.commit()
        return cliente

    @classmethod
    def actualizar(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE {cls.__TABLA} SET nombres = %(nombres)s, apellidos = %(apellidos)s, telefono = %(telefono)s, sexo = %(sexo)s, usuario = %(usuario)s WHERE id = %(id)s", data)
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
    def obtener_direcciones(cls, id):
        with conn.cursor() as cur:
            data = cur.execute(f"SELECT * FROM direcciones_de_entrega WHERE cliente = %s ", (id,))
            return data.fetchall()
            
    @classmethod
    def agregar_direccion(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO direcciones_de_entrega(nombre, descripcion, provincia, departamento, url, cliente) VALUES(%(nombre)s, %(descripcion)s, %(provincia)s, %(departamento)s, %(url)s, %(cliente)s)", data)
        conn.commit()

    @classmethod
    def actualizar_direccion(cls, data):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE direcciones_de_entrega SET nombre = %(nombre)s, descripcion = %(descripcion)s, provincia = %(provincia)s, departamento = %(departamento)s, url = %(url)s WHERE id = %(id)s", data)
        conn.commit()

    @classmethod
    def eliminar_direccion(cls, id):
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM direcciones_de_entrega WHERE id = %s ", (id,))
        conn.commit()