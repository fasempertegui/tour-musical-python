import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaPrincipal(ttk.Frame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)

        self.controlador = controlador

        titulo_fuente = Font(size=13, weight="bold")
        self.titulo_label = ttk.Label(self, font=titulo_fuente)
        
        self.default_padding = {"padx": 10, "pady": 5}

        self.boton_atras = ttk.Button(self, text="Volver", command=self.regresar)

    def regresar(self):
        self.controlador.regresar()