from utils.utils_vista import VistaUtils

import tkinter as tk
import customtkinter as ctk


class VistaExplorar(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="Tu ubicacion")
        self.titulo_label.pack()

        instrucciones = ctk.CTkLabel(self, text="Haz doble clic en un evento para mas detalles")
        instrucciones.pack(**VistaUtils.padding)

        tab = ctk.CTkTabview(self, text_color="#2F242C", segmented_button_selected_color="#A1A892", segmented_button_selected_hover_color="#9ca686")
        tab_todos = tab.add("Todos")
        tab_futuros = tab.add("Futuros")
        tab_finalizados = tab.add("Finalizados")

        self.listbox_todos = tk.Listbox(tab_todos)
        self.listbox_todos.bind("<Double-Button-1>", self._seleccionar_evento_todos)
        self.listbox_todos.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        self.listbox_todos.pack()

        self.listbox_futuros = tk.Listbox(tab_futuros)
        self.listbox_futuros.bind("<Double-Button-1>", self._seleccionar_evento_futuros)
        self.listbox_futuros.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        self.listbox_futuros.pack()

        self.listbox_finalizados = tk.Listbox(tab_finalizados)
        self.listbox_finalizados.bind("<Double-Button-1>", self._seleccionar_evento_finalizados)
        self.listbox_finalizados.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        self.listbox_finalizados.pack()

        tab.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        tab.pack()

        self._actualizar_eventos()

        self.boton_atras = VistaUtils.crear_boton_atras(self)
        self.boton_atras.configure(command=self.regresar)
        self.boton_atras.pack()

    def regresar(self):
        self.controlador.regresar()

    def _actualizar_eventos(self):
        eventos_todos = self.controlador.obtener_eventos()
        eventos_futuros = self.controlador.obtener_eventos_futuros()
        eventos_finalizados = self.controlador.obtener_eventos_finalizados()
        self.listbox_todos.delete(0, tk.END)
        self.listbox_futuros.delete(0, tk.END)
        self.listbox_finalizados.delete(0, tk.END)
        for evento in eventos_todos:
            self.listbox_todos.insert(tk.END, evento.nombre)
        for evento in eventos_futuros:
            self.listbox_futuros.insert(tk.END, evento.nombre)
        for evento in eventos_finalizados:
            self.listbox_finalizados.insert(tk.END, evento.nombre)

    def _obtener_evento_seleccionado(self, lista):
        indice = lista.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def _seleccionar_evento_todos(self, event):
        eventos = self.controlador.obtener_eventos()
        indice = self._obtener_evento_seleccionado(self.listbox_todos)
        evento = eventos[indice]
        self.controlador.seleccionar_evento(evento)

    def _seleccionar_evento_futuros(self, event):
        eventos = self.controlador.obtener_eventos_futuros()
        indice = self._obtener_evento_seleccionado(self.listbox_futuros)
        evento = eventos[indice]
        self.controlador.seleccionar_evento(evento)

    def _seleccionar_evento_finalizados(self, event):
        eventos = self.controlador.obtener_eventos_finalizados()
        indice = self._obtener_evento_seleccionado(self.listbox_finalizados)
        evento = eventos[indice]
        self.controlador.seleccionar_evento(evento)
