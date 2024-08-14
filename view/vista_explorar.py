from utils.utils_vista import VistaUtils

import tkinter as tk
import customtkinter as ctk


class VistaExplorar(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="Explorar eventos")
        self.titulo_label.pack()

        instrucciones = ctk.CTkLabel(self, text="Haz doble clic en un evento para mas detalles")
        instrucciones.pack(**VistaUtils.padding)

        tab = ctk.CTkTabview(self, text_color="#2F242C", segmented_button_selected_color="#A1A892", segmented_button_selected_hover_color="#9ca686")
        tab_todos = tab.add("Todos")
        tab_futuros = tab.add("Futuros")
        tab_finalizados = tab.add("Finalizados")

        self.listbox_todos = tk.Listbox(tab_todos)
        self.listbox_todos.bind("<Double-Button-1>", lambda event: self._ir_evento_seleccionado(event, self._obtener_eventos_todos, self.listbox_todos))
        self.listbox_todos.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        self.listbox_todos.pack()

        self.listbox_futuros = tk.Listbox(tab_futuros)
        self.listbox_futuros.bind("<Double-Button-1>", lambda event: self._ir_evento_seleccionado(event, self._obtener_eventos_futuros, self.listbox_futuros))
        self.listbox_futuros.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        self.listbox_futuros.pack()

        self.listbox_finalizados = tk.Listbox(tab_finalizados)
        self.listbox_finalizados.bind("<Double-Button-1>", lambda event: self._ir_evento_seleccionado(event, self._obtener_eventos_finalizados, self.listbox_finalizados))
        self.listbox_finalizados.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        self.listbox_finalizados.pack()

        tab.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        tab.pack()

        self._actualizar_eventos()

        self.boton_atras = VistaUtils.crear_boton_atras(self)
        self.boton_atras.configure(command=self._regresar)
        self.boton_atras.pack()

    # Privados

    def _ir_evento_seleccionado(self, event, funcion, listbox):
        evento = VistaUtils.obtener_evento_seleccionado(event, funcion, listbox)
        self.controlador.ir_evento_seleccionado(evento)

    def _obtener_eventos_todos(self):
        return self.controlador.obtener_eventos()

    def _obtener_eventos_futuros(self):
        return self.controlador.obtener_eventos_futuros()

    def _obtener_eventos_finalizados(self):
        return self.controlador.obtener_eventos_finalizados()

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

    # Navegacion

    def _regresar(self):
        self.controlador.regresar()
