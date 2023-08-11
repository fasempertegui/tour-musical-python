from view.vista_principal import VistaPrincipal

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaInicio(VistaPrincipal):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label["text"] = "Tour Musical"
        self.titulo_label.pack(**self.default_padding)

        fuente_descripcion = Font(size=12)
        descripcion = ttk.Label(self, text="Descubre eventos musicales, planifica rutas y comparte tu experiencia de manera eficiente y agradable con esta app", font=fuente_descripcion, wraplength=250)
        descripcion.pack(padx=10, pady=15)

        frame_botones = ttk.Frame(self)

        boton_explorar = ttk.Button(frame_botones, text="Explorar eventos", command=self.ir_a_explorar)
        boton_explorar.grid(row=0, column=0, pady=5)

        boton_buscar = ttk.Button(frame_botones, text="Buscar eventos", command=self.ir_a_busqueda)
        boton_buscar.grid(row=1, column=0, pady=5)

        boton_asistidos = ttk.Button(frame_botones, text="Eventos asistidos", command=self.ir_a_asistidos)
        boton_asistidos.grid(row=2, column=0, pady=5)

        frame_botones.pack(padx=10, pady=15)

    def ir_a_explorar(self):
        self.controlador.ir_a_explorar()

    def ir_a_busqueda(self):
        self.controlador.ir_a_busqueda()

    def ir_a_asistidos(self):
        self.controlador.ir_a_asistidos()