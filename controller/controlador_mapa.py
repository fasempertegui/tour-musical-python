from utils.utils_sesion import SesionUtils
from utils.utils_mapa import MapaUtils


class ControladorMapa():
    def __init__(self, app, ubicacion=None):
        self.app = app
        self.ubicacion = ubicacion

    # Publicos

    def obtener_ubicacion_actual(self):
        return self.ubicacion

    def obtener_ruta(self, lat_origen, lon_origen, lat_destino, lon_destino):
        return MapaUtils.obtener_ruta(lat_origen, lon_origen, lat_destino, lon_destino)

    def obtener_configuracion_usuario(self):
        usuario = SesionUtils.obtener_usuario_sesion(self.app.cliente)
        return usuario.configuracion_usuario

    def regresar(self):
        self.app.volver_vista_anterior()
