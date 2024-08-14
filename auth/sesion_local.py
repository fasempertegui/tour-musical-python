import json
import os


class SesionLocal:
    @staticmethod
    def existe_sesion_local():
        return os.path.exists('sesion.json')

    @staticmethod
    def obtener_sesion_local():
        if os.path.exists('sesion.json'):
            with open('sesion.json', 'r') as file:
                data = json.load(file)
                return data.get("id_sesion")

    @staticmethod
    def guardar_sesion_local(id_sesion):
        with open('sesion.json', 'w') as file:
            json.dump({"id_sesion": id_sesion}, file)

    @staticmethod
    def eliminar_sesion_local():
        if os.path.exists('sesion.json'):
            os.remove('sesion.json')
