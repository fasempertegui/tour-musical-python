import tkinter as tk
import customtkinter as ctk

from utils.utils_vista import VistaUtils


class VistaAsistidos(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="Tu ubicacion")
        self.titulo_label.pack()

        instrucciones = ctk.CTkLabel(self, text="Haz doble clic en un evento para mas detalles")
        instrucciones.pack(**VistaUtils.padding)

        self.listbox = tk.Listbox(self)
        self.listbox.bind("<Double-Button-1>", self._seleccionar_evento)
        self.listbox.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        self.listbox.pack()

        self._actualizar_eventos()

        self.master.bind("<<actualizar_asistidos>>", self._actualizar_eventos)

        self.boton_atras = VistaUtils.crear_boton_atras(self)
        self.boton_atras.configure(command=self.regresar)
        self.boton_atras.pack()

    def _actualizar_eventos(self, *args):
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
