from view.vista_principal import VistaPrincipal

import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView


class VistaMapa(VistaPrincipal):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.ubicacion = None

        self.titulo_label["text"] = "Ubicacion del evento"
        self.titulo_label.pack(**self.default_padding)

        frame_mapa = ttk.Frame(self)
        frame_mapa.pack()
        self.mapa = TkinterMapView(frame_mapa, width=270, height=240, corner_radius=1)
        self.mapa.pack()

        self.boton_atras.pack(side='bottom', **self.default_padding)

    def _agregar_marcador(self, coordenadas):
        latitud, longitud = coordenadas.split(",")
        self.mapa.set_position(float(latitud), float(longitud))
        self.mapa.set_marker(float(latitud), float(longitud))
        self.mapa.set_zoom(15)