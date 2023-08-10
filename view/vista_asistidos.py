import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


from view.vista_principal_eventos import VistaPrincipalEventos


class VistaAsistidos(VistaPrincipalEventos):

    def __init__(self, master=None, controlador=None):
        super().__init__(master, controlador)

        self.master = master

        titulo_fuente = Font(size=13, weight="bold")
        self.titulo = ttk.Label(
            self, text="Eventos asistidos", font=titulo_fuente)
        self.titulo.pack(padx=10, pady=5)

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)
        self.listbox.bind("<Double-Button-1>", self.seleccionar_evento)
        self.listbox.pack(padx=10, pady=15)

        self.actualizar_eventos()

        self.boton_atras = ttk.Button(
            self, text="Volver", command=self.regresar
        )
        self.boton_atras.pack(padx=10, pady=5)