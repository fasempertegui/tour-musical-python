from auth.sesion import Sesion

from controller.controlador_ajustes import ControladorAjustes
from controller.controlador_asistidos import ControladorAsistidos
from controller.controlador_busqueda import ControladorBusqueda
from controller.controlador_explorar import ControladorExplorar

from utils.utils_sesion import SesionUtils

from view.views.vista_ajustes import VistaAjustes
from view.views.vista_asistidos import VistaAsistidos
from view.views.vista_busqueda import VistaBusqueda
from view.views.vista_explorar import VistaExplorar


class ControladorInicio():
    def __init__(self, app):
        self.app = app

    # Publicos

    def cerrar_sesion(self):
        id_sesion = Sesion.obtener_sesion_local()
        Sesion.eliminar_sesion(self.app.cliente, id_sesion)
        self.app.ir_a_login()

    def obtener_nombre_usuario(self):
        return SesionUtils.obtener_usuario_sesion(self.app.cliente).nombre_usuario

    def ir_a_ajustes(self):
        self.app.cambiar_vista(ControladorAjustes, VistaAjustes)

    def ir_a_explorar(self):
        self.app.cambiar_vista(ControladorExplorar, VistaExplorar)

    def ir_a_busqueda(self):
        self.app.cambiar_vista(ControladorBusqueda, VistaBusqueda)

    def ir_a_asistidos(self):
        self.app.cambiar_vista(ControladorAsistidos, VistaAsistidos)
