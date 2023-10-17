from view.vista_principal import VistaPrincipal

import tkinter as tk
import customtkinter as ctk


class VistaAjustes(VistaPrincipal):
    def __init__(self, master=None, controlador=None):
        super().__init__(master, controlador)

        self.titulo_label.configure(text="Ajustes")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        self.boton_atras.pack_configure(side='bottom', **self.default_padding)
        self.boton_atras.pack()
