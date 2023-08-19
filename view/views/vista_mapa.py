from view.vista_principal import VistaPrincipal
from utils.ruta import obtener_coordenadas_ruta

import tkinter as tk
import customtkinter as ctk
from tkintermapview import TkinterMapView


class VistaMapa(VistaPrincipal):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.configure(text="Ubicacion del evento")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        frame_principal = ctk.CTkFrame(self, fg_color="transparent")
        frame_principal.pack_configure(fill="both", expand=True)
        frame_principal.pack()

        self.mapa = TkinterMapView(frame_principal, corner_radius=0)
        self.mapa.pack(**self.default_padding, fill="both", expand=True)

        self.check_var = tk.BooleanVar()

        self.check_agregar_ruta = ctk.CTkCheckBox(
            frame_principal, variable=self.check_var, command=self._on_check, checkbox_width=12,
            checkbox_height=12)
        self.check_agregar_ruta.pack()

        self.master.bind("<<Mapa>>", self._inicializar)

        self.boton_atras.pack_configure(side='bottom', **self.default_padding)
        self.boton_atras.pack()

    def _inicializar(self, *args):
        self.mapa.delete_all_marker()
        self.mapa.delete_all_path()
        self.check_agregar_ruta.configure(text="Mostrar ruta")
        self.check_var.set(False)
        # A implementar: que el usuario pueda agregar un marcador determinando el origen
        coordenadas_origen = [-24.780302846326197, -65.42832560657044]
        coordenadas_evento = self.controlador.obtener_ubicacion_actual().coordenadas
        self._establecer_vista(coordenadas_evento)
        self.ruta = obtener_coordenadas_ruta(
            coordenadas_origen[0], coordenadas_origen[1], coordenadas_evento[0], coordenadas_evento[1])

    def _establecer_vista(self, coordenadas_evento):
        # coordenadas[0] -> latitud | coordenadas[1] -> longitud
        self.mapa.set_position(coordenadas_evento[0], coordenadas_evento[1])
        self.mapa.set_marker(coordenadas_evento[0], coordenadas_evento[1])
        self.mapa.set_zoom(15)

    def _agregar_ruta(self):
        self.mapa.set_path(self.ruta)

    def _quitar_ruta(self):
        self.mapa.delete_all_path()

    def _on_check(self):
        if self.check_var.get():
            self.check_agregar_ruta.configure(text="Ocultar ruta")
            self._agregar_ruta()
        else:
            self.check_agregar_ruta.configure(text="Mostrar ruta")
            self._quitar_ruta()
