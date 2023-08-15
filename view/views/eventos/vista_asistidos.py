from view.views.vista_eventos import VistaEventos

import tkinter as tk
from tkinter import ttk


class VistaAsistidos(VistaEventos):
    def __init__(self, master=None, controlador=None):
        super().__init__(master, controlador)

        self.titulo_label["text"] = "Eventos asistidos"
        self.titulo_label.pack(**self.default_padding)

        # Listbox en la clase padre
        self.listbox.bind("<Double-Button-1>", self.seleccionar_evento)
        self.listbox.pack(**self.default_padding, fill="both", expand="true")

        self.actualizar_eventos()

        # Boton en la clase padre, padre
        self.boton_atras.pack(side="bottom", **self.default_padding)

    def actualizar_eventos(self):
        eventos = self.controlador.obtener_eventos_asistidos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    def seleccionar_evento(self, event):
        lista = self.controlador.obtener_eventos_asistidos()
        indice = self.obtener_evento_seleccionado()
        evento = lista[indice]
        self.controlador.seleccionar_evento(evento)
