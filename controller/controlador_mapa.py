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
        usuario_actual = SesionUtils.obtener_usuario_sesion(self.app.cliente)
        if usuario_actual:
            return usuario_actual.configuracion_usuario
        else:
            print("El usuario no existe o la sesion es invalida")
            return None

    def regresar(self):
        self.app.volver_vista_anterior()
