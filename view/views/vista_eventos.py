from view.vista_principal import VistaPrincipal

import tkinter as tk
from tkinter import ttk


class VistaEventos(VistaPrincipal):
    def __init__(self, master=None, controlador=None):
        super().__init__(master, controlador)

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)

    def actualizar_eventos(self):
        eventos = self.controlador.obtener_eventos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    def obtener_evento_seleccionado(self):
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None