from controller.controlador_mapa import ControladorMapa
from controller.controlador_principal_info import ControladorPrincipalInfo
from controller.controlador_eventos import ControladorEventos
from controller.controlador_inicio import ControladorInicio
from controller.controlador_busqueda import ControladorBusqueda
from controller.controlador_asistidos import ControladorAsistidos
from controller.controlador_reviews import ControladorReviews
from view.views.vista_mapa import VistaMapa
from view.views.info_eventos.vista_finalizados import VistaFinalizados
from view.views.info_eventos.vista_proximos import VistaProximos
from view.views.eventos.vista_explorar import VistaExplorar
from view.views.vista_inicio import VistaInicio
from view.views.eventos.vista_busqueda import VistaBusqueda
from view.views.eventos.vista_asistidos import VistaAsistidos
from view.views.vista_reviews import VistaReviews
from model.ubicacion import Ubicacion
from model.evento import Evento
from model.usuario import Usuario
from model.review import Review
import tkinter as tk

'''
El proyecto no esta finalizado. 
Carece de un diseño moderno y atractivo, aun faltan caracteristicas (como el planificado de rutas) y otras fueron modificadas (como mostrar un mapa -con su respectivo marcador- para cada evento, en vez de un mapa para todos los eventos)
que personalmente si tuviera que -re-implementarlas no representaria un desafio mayor.
Simplemente decidi invertir mas tiempo en utilizar e implementar correctamente el patron de diseño MVC, la programacion orientada a objetos y en que todo funcione correctamente como lo pensé desde un principio.
'''


class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tour musical")
        self.geometry("330x330")
        self.resizable(False, False)
        self.inicializar()
        # Se utiliza una lista para trackear los frames visitados para poder regresar de manera correcta
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
        controlador_principal_info = ControladorPrincipalInfo(self, eventos, reviews, usuario_logueado)
        controlador_mapa = ControladorMapa(self)
        controlador_busqueda = ControladorBusqueda(self, eventos, ubicaciones)
        controlador_asistidos = ControladorAsistidos(self, eventos, ubicaciones, usuario_logueado)
        controlador_reviews = ControladorReviews(self, usuarios, reviews)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_eventos = VistaExplorar(self, controlador_eventos)
        # Controlador compartido por ambas vistas
        self.vista_finalizados = VistaFinalizados(self, controlador_principal_info)
        self.vista_proximos = VistaProximos(self, controlador_principal_info)
        self.vista_mapa = VistaMapa(self, controlador_mapa)
        self.vista_busqueda = VistaBusqueda(self, controlador_busqueda)
        self.vista_asistidos = VistaAsistidos(self, controlador_asistidos)
        self.vista_reviews = VistaReviews(self, controlador_reviews)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_eventos)
        self.ajustar_frame(self.vista_finalizados)
        self.ajustar_frame(self.vista_proximos)
        self.ajustar_frame(self.vista_mapa)
        self.ajustar_frame(self.vista_busqueda)
        self.ajustar_frame(self.vista_asistidos)
        self.ajustar_frame(self.vista_reviews)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky='nsew')

    def cambiar_frame(self, frame_destino):
        # Si no controlo que el frame no este en el historial (que puede ocurrir al avanzar dos veces y luego retroceder) el frame se duplicara y no se podra regresar
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
