import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


from view.vista_principal_eventos import VistaPrincipalEventos


class VistaAsistidos(VistaPrincipalEventos):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        titulo_fuente = Font(size=13, weight="bold")
        titulo = ttk.Label(self, text="Eventos asistidos", font=titulo_fuente)
        titulo.pack(padx=10, pady=5)

        # Listbox en la clase padre
        self.listbox.bind("<Double-Button-1>", self.seleccionar_evento)
        self.listbox.pack(padx=10, pady=15)

        self.actualizar_eventos()

        # Boton en la clase padre
        self.boton_atras.pack(padx=10, pady=5)

    def actualizar_eventos(self):
        eventos = self.obtener_eventos_asistidos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    def seleccionar_evento(self, event):
        lista = self.obtener_eventos_asistidos()
        indice = self.obtener_evento_seleccionado()
        evento = lista[indice]
        self.controlador.seleccionar_evento(evento)

    def obtener_eventos_asistidos(self):
        return self.controlador.obtener_eventos_asistidos()