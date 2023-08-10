from controller.controlador_mapa import ControladorMapa
from controller.controlador_info_anteriores import ControladorInfoAnteriores
from controller.controlador_info_proximos import ControladorInfoProximos
from controller.controlador_eventos import ControladorEventos
from controller.controlador_inicio import ControladorInicio
from controller.controlador_busqueda import ControladorBusqueda
from controller.controlador_asistidos import ControladorAsistidos
from view.vista_mapa import VistaMapa
from view.vista_info_anteriores import VistaInfoAnteriores
from view.vista_info_proximos import VistaInfoProximos
from view.vista_eventos import VistaEventos
from view.vista_inicio import VistaInicio
from view.vista_busqueda import VistaBusqueda
from view.vista_asistidos import VistaAsistidos
from model.ubicacion import Ubicacion
from model.evento import Evento
from model.usuario import Usuario
import tkinter as tk


class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tour musical")
        self.geometry("330x330")
        self.resizable(False, False)
        self.inicializar()
        self.historial_vistas = []
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        eventos = Evento.cargar_eventos("data/eventos.json")
        ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicaciones.json")
        usuarios = Usuario.cargar_usuario("data/usuarios.json")

        usuario_logueado = usuarios[1]

        controlador_inicio = ControladorInicio(self)
        controlador_eventos = ControladorEventos(self, eventos, ubicaciones)
        controlador_info_anteriores = ControladorInfoAnteriores(self)
        controlador_info_proximos = ControladorInfoProximos(self)
        controlador_mapa = ControladorMapa(self)
        controlador_busqueda = ControladorBusqueda(self, eventos, ubicaciones)
        controlador_asistidos = ControladorAsistidos(self, eventos, ubicaciones, usuario_logueado)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_eventos = VistaEventos(self, controlador_eventos)
        self.vista_info_anteriores = VistaInfoAnteriores(self, controlador_info_anteriores)
        self.vista_info_proximos = VistaInfoProximos(self, controlador_info_proximos)
        self.vista_mapa = VistaMapa(self, controlador_mapa)
        self.vista_busqueda = VistaBusqueda(self, controlador_busqueda)
        self.vista_asistidos = VistaAsistidos(self, controlador_asistidos)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_eventos)
        self.ajustar_frame(self.vista_info_anteriores)
        self.ajustar_frame(self.vista_info_proximos)
        self.ajustar_frame(self.vista_mapa)
        self.ajustar_frame(self.vista_busqueda)
        self.ajustar_frame(self.vista_asistidos)

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
