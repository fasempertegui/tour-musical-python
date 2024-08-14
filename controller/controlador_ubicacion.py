from utils.decoradores import requiere_sesion_valida
from utils.utils_sesion import SesionUtils


class ControladorUbicacion():
    def __init__(self, app):
        self.app = app
        self.coordenadas = None

    # Publicos

    def establecer_coordenadas(self, coordenadas):
        self.coordenadas = coordenadas

    @requiere_sesion_valida
    def guardar_cambios(self):
        usuario = SesionUtils.obtener_usuario_sesion(self.app.cliente)
        actualizacion = {"$set": {"configuracion_usuario": {"ubicacion": self.coordenadas}}}
        usuario.actualizar_usuario(self.app.cliente, actualizacion)

    def regresar(self):
        self.app.volver_vista_anterior()
