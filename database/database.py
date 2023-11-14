from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

class Conexion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            try:
                cls._instancia.cliente = MongoClient(os.getenv("HOST"), int(os.getenv("PUERTO")))
                cls._instancia.cliente.admin.command('ismaster')
                print("Conexión exitosa a la base de datos.")
            except ConnectionFailure as e:
                raise RuntimeError("Error de conexión a la base de datos:", e)
        return cls._instancia

    def obtener_cliente(self):
        return self.cliente[os.getenv("BD_NOMBRE")]