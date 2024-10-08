import tkinter as tk
import customtkinter as ctk

from utils.utils_vista import VistaUtils


class VistaBusqueda(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="Busqueda de eventos")
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
                radiobutton_height=12,
                radiobutton_width=12,
                border_width_unchecked=3,
                border_width_checked=3,
                border_color="#A1A892",
                hover_color="#9ca686",
                fg_color="#7a8a58"

            ).grid(row=0, column=index, padx=3, pady=3)

        frame_entry_box = ctk.CTkFrame(frame_principal_opciones, fg_color="transparent")
        frame_entry_box.pack_configure(**VistaUtils.padding)
        frame_entry_box.pack()

        self.entry_box = ctk.CTkEntry(frame_entry_box, placeholder_text="Tu busqueda")
        self.entry_box.bind("<Button>", self._restablecer_eventos)
        self.entry_box.pack_configure(side='left', **VistaUtils.padding)
        self.entry_box.pack()

        boton_busqueda = ctk.CTkButton(frame_entry_box, text="Buscar", command=self._buscar_eventos, **VistaUtils.estilo_boton)
        boton_busqueda.pack_configure(side='right', **VistaUtils.padding)
        boton_busqueda.pack()

        instrucciones = ctk.CTkLabel(self, text="Haz doble clic en un evento para mas detalles")
        instrucciones.pack_configure(**VistaUtils.padding)
        instrucciones.pack()

        self.listbox = tk.Listbox(self)
        self.listbox.bind("<Double-Button-1>", lambda event: self._ir_evento_seleccionado(event, self._obtener_eventos_busqueda, self.listbox))
        self.listbox.pack_configure(**VistaUtils.padding, fill="both", expand="true")
        self.listbox.pack()

        self._actualizar_eventos()

        self.boton_atras = VistaUtils.crear_boton_atras(self)
        self.boton_atras.configure(command=self._regresar)
        self.boton_atras.pack()

    # Privados

    def _restablecer_eventos(self, *args):
        self.controlador.restablecer_eventos()
        self._actualizar_eventos()

    def _buscar_eventos(self):
        criterio = self.opcion_elegida.get().lower()
        texto_busqueda = self.entry_box.get().lower()
        eventos_filtrados = self.controlador.buscar_eventos(criterio, texto_busqueda)
        self.listbox.delete(0, tk.END)
        for evento in eventos_filtrados:
            self.listbox.insert(tk.END, evento.nombre)

    def _obtener_eventos_busqueda(self):
        return self.controlador.obtener_eventos_busqueda()

    def _actualizar_eventos(self):
        eventos = self.controlador.obtener_eventos_busqueda()
        self.listbox.delete(0, tk.END)
        for evento in eventos:
            self.listbox.insert(tk.END, evento.nombre)

    # Navegacion

    def _ir_evento_seleccionado(self, event, funcion, listbox):
        evento = VistaUtils.obtener_evento_seleccionado(event, funcion, listbox)
        self.controlador.ir_evento_seleccionado(evento)

    def _regresar(self):
        self.controlador.regresar()
