import tkinter as tk
from tkinter import ttk

'''

vista_eventos, vista_busqueda y vista_asistidos comparten algunos métodos por lo que me parecio conveniente implementar una clase padre

'''


class VistaPrincipalEventos(ttk.Frame):
    def __init__(self, master=None, controlador=None):

        super().__init__(master)

        self.master = master
        self.controlador = controlador

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)
        self.listbox.bind("<Double-Button-1>", self.seleccionar_evento)

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
        lista = self.obtener_eventos()
        indice = self.obtener_evento_seleccionado()
        evento = lista[indice]
        self.controlador.seleccionar_evento(evento)

    def obtener_eventos(self):
        return self.controlador.obtener_eventos()

    def obtener_eventos_proximos(self):
        return self.controlador.obtener_eventos_proximos()

    def obtener_eventos_finalizados(self):
        return self.controlador.obtener_eventos_finalizados()
    
    def regresar(self):
        self.controlador.regresar()