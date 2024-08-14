from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os


class Conexion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            try:
                host = os.getenv("HOST")
                puerto = int(os.getenv("PUERTO"))
                bd_nombre = os.getenv("BD_NOMBRE")

                if not host or not puerto or not bd_nombre:
                    raise RuntimeError("Error en las variables de entorno HOST, PUERTO y/o BD_NOMBRE")

                cls._instancia.cliente = MongoClient(host, puerto)
                cls._instancia.cliente.admin.command('ismaster')
                print("Conexión exitosa a la base de datos.")
            except ConnectionFailure as e:
                raise RuntimeError("Error de conexión a la base de datos: " + str(e))
        return cls._instancia

    def obtener_cliente(self):
        bd_nombre = os.getenv("BD_NOMBRE")
        if not bd_nombre:
            raise RuntimeError("Error en la variable de entorno BD_NOMBRE")
        return self.cliente[bd_nombre]
