from view.vista_principal import VistaPrincipal

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaInfoEvento(VistaPrincipal):
    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.pack(**self.default_padding)

        descripcion_fuente = Font(size=10)
        self.descripcion_label = ttk.Label(self, font=descripcion_fuente, wraplength=250)
        self.descripcion_label.pack(**self.default_padding)

        self.info_evento_label = ttk.Label(self)
        self.info_evento_label.pack(**self.default_padding)