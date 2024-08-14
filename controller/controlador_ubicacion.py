from utils.decoradores import requiere_sesion_valida
from utils.utils_sesion import SesionUtils


class ControladorUbicacion():
    def __init__(self, app):
        self.app = app
        self.coordenadas = None

    # Publicos

    def obtener_coordenadas(self):
        return self.coordenadas

    def establecer_coordenadas(self, coordenadas):
        self.coordenadas = coordenadas

    @requiere_sesion_valida
    def guardar_cambios(self):
        usuario_actual = SesionUtils.obtener_usuario_sesion(self.app.cliente)
        if usuario_actual:
            actualizacion = {"$set": {"configuracion_usuario": {"ubicacion": self.coordenadas}}}
            usuario_actual.actualizar_usuario(self.app.cliente, actualizacion)
        else:
            print("El usuario no existe o la sesion es invalida")

    def regresar(self):
        self.app.volver_vista_anterior()
