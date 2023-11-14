from controller.controllers.controlador_mapa import ControladorMapa
from controller.controllers.controlador_proximos import ControladorProximos
from controller.controllers.controlador_finalizados import ControladorFinalizados
from controller.controllers.controlador_explorar import ControladorExplorar
from controller.controllers.controlador_inicio import ControladorInicio
from controller.controllers.controlador_busqueda import ControladorBusqueda
from controller.controllers.controlador_asistidos import ControladorAsistidos
from controller.controllers.controlador_reviews import ControladorReviews
from controller.controllers.controlador_escribir_review import ControladorEscribirReview
from controller.controllers.controlador_ajustes import ControladorAjustes
from controller.controllers.controlador_login import ControladorLogin 

from view.views.vista_mapa import VistaMapa
from view.views.vista_finalizados import VistaFinalizados
from view.views.vista_proximos import VistaProximos
from view.views.vista_explorar import VistaExplorar
from view.views.vista_inicio import VistaInicio
from view.views.vista_busqueda import VistaBusqueda
from view.views.vista_asistidos import VistaAsistidos
from view.views.vista_reviews import VistaReviews
from view.views.vista_escribir_review import VistaEscribirReview
from view.views.vista_ajustes import VistaAjustes
from view.views.vista_login import VistaLogin

from database.database import Conexion

import customtkinter as ctk

ctk.set_appearance_mode("dark")

class Aplicacion(ctk.CTk):

    def __init__(self):

        conexion = Conexion()
        self.cliente = conexion.obtener_cliente()

        ctk.CTk.__init__(self)
        self.title("Tour musical")
        self.geometry("450x450")
        # self.resizable(False, False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.inicializar()

        self.bind("<<Logout>>", self.inicializar)
        self.bind("<<Login>>", self.renderizar)

    def inicializar(self, *args):
        self.historial_vistas = []

        controlador_login = ControladorLogin(self)
        self.vista_login = VistaLogin(self, controlador_login)
        
        self.cambiar_frame(self.vista_login)

    def renderizar(self, *args):
        self.historial_vistas = []

        controlador_inicio = ControladorInicio(self)
        controlador_explorar = ControladorExplorar(self)
        controlador_proximos = ControladorProximos(self)
        controlador_finalizados = ControladorFinalizados(self)
        controlador_mapa = ControladorMapa(self)
        controlador_busqueda = ControladorBusqueda(self)
        controlador_asistidos = ControladorAsistidos(self)
        controlador_reviews = ControladorReviews(self)
        controlador_escribir_review = ControladorEscribirReview(self)
        controlador_ajustes = ControladorAjustes(self)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_explorar = VistaExplorar(self, controlador_explorar)
        self.vista_proximos = VistaProximos(self, controlador_proximos)
        self.vista_finalizados = VistaFinalizados( self, controlador_finalizados)
        self.vista_mapa = VistaMapa(self, controlador_mapa)
        self.vista_busqueda = VistaBusqueda(self, controlador_busqueda)
        self.vista_asistidos = VistaAsistidos(self, controlador_asistidos)
        self.vista_reviews = VistaReviews(self, controlador_reviews)
        self.vista_escribir_review = VistaEscribirReview(self, controlador_escribir_review)
        self.vista_ajustes = VistaAjustes(self, controlador_ajustes)

        self.cambiar_frame(self.vista_inicio)

    def cambiar_frame(self, frame_destino):
        if frame_destino not in self.historial_vistas:
            self.historial_vistas.append(frame_destino)
        frame_destino.grid(row=0, column=0, sticky='nsew')
        frame_destino.tkraise()

    def volver_frame_anterior(self):
        if len(self.historial_vistas) > 1:
            self.historial_vistas.pop()
            vista_anterior = self.historial_vistas[-1]
            self.cambiar_frame(vista_anterior)


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.mainloop()
