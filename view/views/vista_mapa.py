from view.vista_principal import VistaPrincipal

import tkinter as tk
import customtkinter as ctk
from tkintermapview import TkinterMapView


class VistaMapa(VistaPrincipal):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.configure(text="Ubicacion del evento")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        self.frame_principal = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_principal.pack_configure(fill="both", expand=True)
        self.frame_principal.pack()

        self.mapa = TkinterMapView(self.frame_principal, corner_radius=0)
        self.mapa.pack(**self.default_padding, fill="both", expand=True)

        self.check_var = tk.BooleanVar()

        self.check_agregar_ruta = ctk.CTkCheckBox(
            self.frame_principal, variable=self.check_var, command=self._on_check, checkbox_width=12,
            checkbox_height=12)
        self.check_agregar_ruta.pack()

        self._inicializar()

        self.boton_atras.pack_configure(side='bottom', **self.default_padding)
        self.boton_atras.pack()

    def _inicializar(self, *args):
        self.mapa.delete_all_marker()
        self.mapa.delete_all_path()
        self.check_agregar_ruta.configure(text="Mostrar ruta")
        self.check_var.set(False)
        coordenadas_evento = self.controlador.obtener_ubicacion_actual().coordenadas
        self._establecer_vista(coordenadas_evento)
        configuracion_usuario = self.controlador.obtener_configuracion_usuario()
        if configuracion_usuario["ubicacion"] is not None:
            coordenadas_origen = configuracion_usuario["ubicacion"]
            self.ruta = self.controlador.obtener_ruta(
                coordenadas_origen[0], coordenadas_origen[1],
                coordenadas_evento[0], coordenadas_evento[1]
            )
        else:
            label_alerta = ctk.CTkLabel(self.frame_principal, text="Establece una ubicacion en ajustes para ver la ruta", text_color="red")
            label_alerta.pack(after=self.check_agregar_ruta)
            self.check_agregar_ruta.configure(state=tk.DISABLED)

    def _establecer_vista(self, coordenadas_evento):
        # coordenadas[0] -> latitud | coordenadas[1] -> longitud
        self.mapa.set_position(coordenadas_evento[0], coordenadas_evento[1])
        self.mapa.set_marker(coordenadas_evento[0], coordenadas_evento[1])
        self.mapa.set_zoom(15)

    def _on_check(self):
        if self.check_var.get():
            self.check_agregar_ruta.configure(text="Ocultar ruta")
            self.mapa.set_path(self.ruta)
        else:
            self.check_agregar_ruta.configure(text="Mostrar ruta")
            self.mapa.delete_all_path()
