import psycopg

conn = psycopg.connect("dbname=ecommercev2 user=postgres password=nielsroy1 host=localhost port=5432")

# class Conexion:

#     __HOST = "localhost"
#     __USER = "postgres"
#     __PASSWORD = "nielsroy1"
#     __PORT = "5432"
#     __DATABASE = "ecommerce"

#     @classmethod
#     def obtener_conexion(self):
#         print("Obteniendo conexion...")
#         return psycopg.connect("dbname=ecommerce user=postgres password=nielsroy1 host=localhost port=5432")
        