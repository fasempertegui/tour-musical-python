from controller.controlador_mapa import ControladorMapa
from controller.controlador_info_finalizados import ControladorInfoFinalizados
from controller.controlador_info_proximos import ControladorInfoProximos
from controller.controlador_eventos import ControladorEventos
from controller.controlador_inicio import ControladorInicio
from controller.controlador_busqueda import ControladorBusqueda
from controller.controlador_asistidos import ControladorAsistidos
from controller.controlador_reviews import ControladorReviews
from view.vista_mapa import VistaMapa
from view.vista_info_finalizados import VistaInfoFinalizados
from view.vista_info_proximos import VistaInfoProximos
from view.vista_eventos import VistaEventos
from view.vista_inicio import VistaInicio
from view.vista_busqueda import VistaBusqueda
from view.vista_asistidos import VistaAsistidos
from view.vista_reviews import VistaReviews
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
        self.inicializar()
        # Se utiliza una lista para mantener track de los frames visitados para poder regresar de manera correcta.
        self.historial_vistas = []
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        eventos = Evento.cargar_eventos("data/eventos.json")
        ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        usuarios = Usuario.cargar_usuario("data/usuarios.json")
        reviews = Review.cargar_reviews("data/reviews.json")

        # "Login"
        usuario_logueado = usuarios[0]

        controlador_inicio = ControladorInicio(self)
        controlador_eventos = ControladorEventos(self, eventos, ubicaciones)
        controlador_info_finalizados = ControladorInfoFinalizados(self)
        controlador_info_proximos = ControladorInfoProximos(self)
        controlador_mapa = ControladorMapa(self)
        controlador_busqueda = ControladorBusqueda(self, eventos, ubicaciones)
        controlador_asistidos = ControladorAsistidos(self, eventos, ubicaciones, usuario_logueado)
        controlador_reviews = ControladorReviews(self, reviews, usuarios)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_eventos = VistaEventos(self, controlador_eventos)
        self.vista_info_finalizados = VistaInfoFinalizados(self, controlador_info_finalizados)
        self.vista_info_proximos = VistaInfoProximos(self, controlador_info_proximos)
        self.vista_mapa = VistaMapa(self, controlador_mapa)
        self.vista_busqueda = VistaBusqueda(self, controlador_busqueda)
        self.vista_asistidos = VistaAsistidos(self, controlador_asistidos)
        self.vista_reviews = VistaReviews(self, controlador_reviews)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_eventos)
        self.ajustar_frame(self.vista_info_finalizados)
        self.ajustar_frame(self.vista_info_proximos)
        self.ajustar_frame(self.vista_mapa)
        self.ajustar_frame(self.vista_busqueda)
        self.ajustar_frame(self.vista_asistidos)
        self.ajustar_frame(self.vista_reviews)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky='nsew')

    def cambiar_frame(self, frame_destino):
        # Si no controlo que el frame no este en el historial (que podria ocurrir al avanzar dos veces y luego retroceder) el frame se duplicara y no podre regresar
        if frame_destino not in self.historial_vistas:
            self.historial_vistas.append(frame_destino)
        frame_destino.tkraise()

    def volver_frame_anterior(self):
        if len(self.historial_vistas) > 1:
            # Se elimina el frame actual
            self.historial_vistas.pop()
            # Se recupera el frame anterior
            vista_anterior = self.historial_vistas[-1]
            # Se cambia a dicho frame
            self.cambiar_frame(vista_anterior)


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.mainloop()
