import json
import os


class Token:
    RUTA = 'auth/token.json'

    @classmethod
    def guardar_token(cls, token):
        data = {'token': token}
        with open(cls.RUTA, 'w') as file:
            json.dump(data, file)

    @classmethod
    def obtener_token(cls):
        if not os.path.exists(cls.RUTA):
            return None
        with open(cls.RUTA, 'r') as file:
            data = json.load(file)
        return data.get('token')

    @classmethod
    def eliminar_token(cls):
        if os.path.exists(cls.RUTA):
            os.remove(cls.RUTA)
