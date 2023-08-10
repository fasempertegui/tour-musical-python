import tkinter as tk
from tkinter import ttk

'''

Tanto vista_eventos como vista_busqueda comparten algunos métodos por lo que decidi crear una clase padre de la cual ambas vistas heredarian

'''


class VistaPrincipalEventos(ttk.Frame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)

        self.master = master
        self.controlador = controlador

    def actualizar_eventos(self):
        eventos = self.obtener_eventos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    def obtener_evento_seleccionado(self):
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_evento(self, event):
        indice = self.obtener_evento_seleccionado()
        self.controlador.seleccionar_evento(indice)

    def obtener_eventos(self):
        return self.controlador.obtener_eventos()

    def obtener_eventos_proximos(self):
        return self.controlador.obtener_eventos_proximos()

    def obtener_eventos_anteriores(self):
        return self.controlador.obtener_eventos_anteriores()
    
    def regresar(self):
        self.controlador.regresar()