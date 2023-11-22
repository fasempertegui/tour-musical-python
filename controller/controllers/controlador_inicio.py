from controller.controlador_principal import ControladorPrincipal
from model.usuario import Sesion

from view.views.vista_ajustes import VistaAjustes
from controller.controllers.controlador_ajustes import ControladorAjustes

from view.views.vista_explorar import VistaExplorar
from controller.controllers.controlador_explorar import ControladorExplorar

from view.views.vista_busqueda import VistaBusqueda
from controller.controllers.controlador_busqueda import ControladorBusqueda

from view.views.vista_asistidos import VistaAsistidos
from controller.controllers.controlador_asistidos import ControladorAsistidos

class ControladorInicio(ControladorPrincipal):
    def __init__(self, app):
        super().__init__(app)

    def cerrar_sesion(self):
        self.app.event_generate("<<logout>>")
        Sesion.cerrar_sesion()

    def ir_a_ajustes(self):
        controlador_ajustes = ControladorAjustes(self.app)
        vista_ajustes = VistaAjustes(self.app, controlador_ajustes)
        self.app.cambiar_frame(vista_ajustes)

    def ir_a_explorar(self):
        controlador_explorar = ControladorExplorar(self.app)
        vista_explorar = VistaExplorar(self.app, controlador_explorar)
        self.app.cambiar_frame(vista_explorar)

    def ir_a_busqueda(self):
        controlador_busqueda = ControladorBusqueda(self.app)
        vista_busqueda = VistaBusqueda(self.app, controlador_busqueda)
        self.app.cambiar_frame(vista_busqueda)

    def ir_a_asistidos(self):
        controlador_asistidos = ControladorAsistidos(self.app)
        vista_asistidos = VistaAsistidos(self.app, controlador_asistidos)
        self.app.cambiar_frame(vista_asistidos)