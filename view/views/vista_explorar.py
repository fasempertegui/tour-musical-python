from view.vista_principal import VistaPrincipal

import tkinter as tk
import customtkinter as ctk

class VistaExplorar(VistaPrincipal):
    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.configure(text="Explorar eventos")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        instrucciones = ctk.CTkLabel(self, text="Haz doble clic en un evento para mas detalles")
        instrucciones.pack(**self.default_padding)
        
        tab = ctk.CTkTabview(self, text_color="#2F242C", segmented_button_selected_color="#A1A892", segmented_button_selected_hover_color="#9ca686")
        tab_todos = tab.add("Todos")
        tab_proximos = tab.add("Proximos")
        tab_finalizados = tab.add("Finalizados")

        self.listbox_todos = tk.Listbox(tab_todos)
        self.listbox_todos.bind("<Double-Button-1>", self._seleccionar_evento_todos)
        self.listbox_todos.pack_configure(**self.default_padding, fill="both", expand="true")
        self.listbox_todos.pack()

        self.listbox_proximos = tk.Listbox(tab_proximos)
        self.listbox_proximos.bind("<Double-Button-1>", self._seleccionar_evento_proximos)
        self.listbox_proximos.pack_configure(**self.default_padding, fill="both", expand="true")
        self.listbox_proximos.pack()
        
        self.listbox_finalizados = tk.Listbox(tab_finalizados)
        self.listbox_finalizados.bind("<Double-Button-1>", self._seleccionar_evento_finalizados)
        self.listbox_finalizados.pack_configure(**self.default_padding, fill="both", expand="true")
        self.listbox_finalizados.pack()

        tab.pack_configure(**self.default_padding, fill="both", expand="true")
        tab.pack()

        self._actualizar_eventos()

        self.boton_atras.pack_configure(side='bottom', **self.default_padding)
        self.boton_atras.pack()


    def _actualizar_eventos(self):
        eventos_todos = self.controlador.obtener_eventos()
        eventos_proximos = self.controlador.obtener_eventos_proximos()
        eventos_finalizados = self.controlador.obtener_eventos_finalizados()
        self.listbox_todos.delete(0, tk.END)
        self.listbox_proximos.delete(0, tk.END)
        self.listbox_finalizados.delete(0, tk.END)
        for evento in eventos_todos:
            self.listbox_todos.insert(tk.END, evento.nombre)
        for evento in eventos_proximos:
            self.listbox_proximos.insert(tk.END, evento.nombre)
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

    def _seleccionar_evento_proximos(self, event):
        eventos = self.controlador.obtener_eventos_proximos()
        indice = self._obtener_evento_seleccionado(self.listbox_proximos)
        evento = eventos[indice]
        self.controlador.seleccionar_evento(evento)

    def _seleccionar_evento_finalizados(self, event):
        eventos = self.controlador.obtener_eventos_finalizados()
        indice = self._obtener_evento_seleccionado(self.listbox_finalizados)
        evento = eventos[indice]
        self.controlador.seleccionar_evento(evento)