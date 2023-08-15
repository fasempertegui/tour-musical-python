from controller.controllers.controlador_mapa import ControladorMapa
from controller.controllers.controlador_proximos import ControladorProximos
from controller.controllers.controlador_finalizados import ControladorFinalizados
from controller.controllers.controlador_explorar import ControladorExplorar
from controller.controllers.controlador_inicio import ControladorInicio
from controller.controllers.controlador_busqueda import ControladorBusqueda
from controller.controllers.controlador_asistidos import ControladorAsistidos
from controller.controllers.controlador_reviews import ControladorReviews
from controller.controllers.controlador_escribir_review import ControladorEscribirReview

from view.views.vista_mapa import VistaMapa
from view.views.vista_finalizados import VistaFinalizados
from view.views.vista_proximos import VistaProximos
from view.views.eventos.vista_explorar import VistaExplorar
from view.views.vista_inicio import VistaInicio
from view.views.eventos.vista_busqueda import VistaBusqueda
from view.views.eventos.vista_asistidos import VistaAsistidos
from view.views.vista_reviews import VistaReviews
from view.views.vista_escribir_review import VistaEscribirReview

from model.ubicacion import Ubicacion
from model.evento import Evento
from model.usuario import Usuario
from model.review import Review

import tkinter as tk


class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tour musical")
        self.geometry("330x330")
        self.resizable(False, False)
        self.historial_vistas = []
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

        self.evento_actual = None
        self.ubicacion_actual = None

    def inicializar(self, *args):

        usuarios = Usuario.cargar_usuario("data/usuarios.json")

        datos = {
            "eventos": Evento.cargar_eventos("data/eventos.json"),
            "ubicaciones": Ubicacion.cargar_ubicaciones("data/ubicaciones.json"),
            "reviews": Review.cargar_reviews("data/reviews.json"),
            "usuarios": usuarios,
            "sesion": usuarios[0]
            }

        controlador_inicio = ControladorInicio(self)
        controlador_explorar = ControladorExplorar(self, **datos)
        controlador_proximos = ControladorProximos(self, **datos)
        controlador_finalizados = ControladorFinalizados(self, **datos)
        controlador_mapa = ControladorMapa(self)
        controlador_busqueda = ControladorBusqueda(self, **datos)
        controlador_asistidos = ControladorAsistidos(self, **datos)
        controlador_reviews = ControladorReviews(self, **datos)
        controlador_escribir_review = ControladorEscribirReview(self, **datos)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_explorar = VistaExplorar(self, controlador_explorar)
        self.vista_proximos = VistaProximos(self, controlador_proximos)
        self.vista_finalizados = VistaFinalizados(self, controlador_finalizados)
        self.vista_mapa = VistaMapa(self, controlador_mapa)
        self.vista_busqueda = VistaBusqueda(self, controlador_busqueda)
        self.vista_asistidos = VistaAsistidos(self, controlador_asistidos)
        self.vista_reviews = VistaReviews(self, controlador_reviews)
        self.vista_escribir_review = VistaEscribirReview(self, controlador_escribir_review)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_explorar)
        self.ajustar_frame(self.vista_proximos)
        self.ajustar_frame(self.vista_finalizados)
        self.ajustar_frame(self.vista_mapa)
        self.ajustar_frame(self.vista_busqueda)
        self.ajustar_frame(self.vista_asistidos)
        self.ajustar_frame(self.vista_reviews)
        self.ajustar_frame(self.vista_escribir_review)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky='nsew')

    def cambiar_frame(self, frame_destino):
        if frame_destino not in self.historial_vistas:
            self.historial_vistas.append(frame_destino)
        frame_destino.tkraise()

    def volver_frame_anterior(self):
        if len(self.historial_vistas) > 1:
            self.historial_vistas.pop()
            vista_anterior = self.historial_vistas[-1]
            self.cambiar_frame(vista_anterior)


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.mainloop()
