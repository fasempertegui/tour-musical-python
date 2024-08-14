import tkinter as tk
import customtkinter as ctk

from utils.utils_vista import VistaUtils


class VistaAsistidos(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="Eventos asistidos")
        self.titulo_label.pack()

        instrucciones = ctk.CTkLabel(self, text="Haz doble clic en un evento para mas detalles")
        instrucciones.pack(**VistaUtils.padding)

        self.listbox = tk.Listbox(self)
        self.listbox.bind("<Double-Button-1>", lambda event: self._ir_evento_seleccionado(event, self._obtener_eventos_asistidos, self.listbox))
        self.listbox.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        self.listbox.pack()

        self._actualizar_eventos()

        self.master.bind("<<actualizar_asistidos>>", self._actualizar_eventos)

        self.boton_atras = VistaUtils.crear_boton_atras(self)
        self.boton_atras.configure(command=self.regresar)
        self.boton_atras.pack()

    def regresar(self):
        self.controlador.regresar()

    def _ir_evento_seleccionado(self, event, funcion, listbox):
        evento = VistaUtils.obtener_evento_seleccionado(event, funcion, listbox)
        self.controlador.ir_evento_seleccionado(evento)

    def _obtener_eventos_asistidos(self):
        return self.controlador.obtener_eventos_asistidos()

    def _actualizar_eventos(self, *args):
        eventos = self.controlador.obtener_eventos_asistidos()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)
