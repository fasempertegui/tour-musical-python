from view.vista_principal import VistaPrincipal

import tkinter as tk
import customtkinter as ctk


class VistaAsistidos(VistaPrincipal):
    def __init__(self, master=None, controlador=None):
        super().__init__(master, controlador)

        self.titulo_label.configure(text="Eventos asistidos")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        instrucciones = ctk.CTkLabel(self, text="Haz doble clic en un evento para mas detalles")
        instrucciones.pack(**self.default_padding)

        self.listbox = tk.Listbox(self)
        self.listbox.bind("<Double-Button-1>", self._seleccionar_evento)
        self.listbox.pack_configure(**self.default_padding, fill="both", expand="true")
        self.listbox.pack()

        self._actualizar_eventos()

        self.boton_atras.pack_configure(side='bottom', **self.default_padding)
        self.boton_atras.pack()

    def _actualizar_eventos(self):
        eventos = self.controlador.obtener_eventos_asistidos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    def _obtener_evento_seleccionado(self):
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def _seleccionar_evento(self, event):
        lista = self.controlador.obtener_eventos_asistidos()
        indice = self._obtener_evento_seleccionado()
        evento = lista[indice]
        self.controlador.seleccionar_evento(evento)
