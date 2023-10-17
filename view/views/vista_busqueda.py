from view.vista_principal import VistaPrincipal

import tkinter as tk
import customtkinter as ctk


class VistaBusqueda(VistaPrincipal):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.configure(text="Buscar eventos")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        frame_principal_opciones = ctk.CTkFrame(self)
        frame_principal_opciones.pack()

        label_opciones = ctk.CTkLabel(frame_principal_opciones, text="Filtrar por")
        label_opciones.pack_configure(side="top")
        label_opciones.pack()

        frame_opciones = ctk.CTkFrame(frame_principal_opciones)
        frame_opciones.pack()

        OPCIONES = [
            "Nombre",
            "Artista",
            "Genero"
        ]

        self.opcion_elegida = tk.StringVar(value=OPCIONES[0])

        # Crear los radio buttons de manera dinamica
        for index, opcion in enumerate(OPCIONES):
            ctk.CTkRadioButton(
                frame_opciones,
                text=opcion,
                value=opcion,
                variable=self.opcion_elegida,
                command=self._restablecer_eventos,
                radiobutton_height=12,
                radiobutton_width=12,
                border_width_unchecked=3,
                border_width_checked=3,
                border_color="#A1A892",
                hover_color="#9ca686",
                fg_color="#7a8a58"

            ).grid(row=0, column=index, padx=3, pady=3)

        frame_entry_box = ctk.CTkFrame(frame_principal_opciones, fg_color="transparent")
        frame_entry_box.pack_configure(**self.default_padding)
        frame_entry_box.pack()

        self.entry_box = ctk.CTkEntry(frame_entry_box, placeholder_text="Tu busqueda")
        self.entry_box.pack_configure(side='left', **self.default_padding)
        self.entry_box.pack()

        boton_busqueda = ctk.CTkButton(
            frame_entry_box, text="Buscar", command=self._buscar_eventos, **self.default_button_color)
        boton_busqueda.pack_configure(side='right', **self.default_padding)
        boton_busqueda.pack()

        instrucciones = ctk.CTkLabel(
            self, text="Haz doble clic en un evento para mas detalles")
        instrucciones.pack_configure(**self.default_padding)
        instrucciones.pack()

        self.listbox = tk.Listbox(self)
        self.listbox.bind("<Double-Button-1>", self._seleccionar_evento)
        self.listbox.pack_configure(
            **self.default_padding, fill="both", expand="true")
        self.listbox.pack()

        self._actualizar_eventos()

        self.boton_atras.pack_configure(side='bottom', **self.default_padding)
        self.boton_atras.pack()

    def _restablecer_eventos(self):
        self.controlador.restablecer_eventos()
        self._actualizar_eventos()

    def _actualizar_eventos(self):
        eventos = self.controlador.obtener_eventos()
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
        lista = self.controlador.obtener_eventos()
        indice = self._obtener_evento_seleccionado()
        evento = lista[indice]
        self.controlador.seleccionar_evento(evento)

    def _buscar_eventos(self):
        criterio = self.opcion_elegida.get().lower()
        texto_busqueda = self.entry_box.get().lower()
        # Filtra la lista de todos los eventos
        eventos_filtrados = self.controlador.buscar_eventos(criterio, texto_busqueda)
        # Actualiza la listbox con los resultados de la busqueda
        self.listbox.delete(0, tk.END)
        for evento in eventos_filtrados:
            self.listbox.insert(tk.END, evento.nombre)