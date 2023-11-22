from view.vista_principal import VistaPrincipal

import customtkinter as ctk


class VistaProximos(VistaPrincipal):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        self.descripcion_label = ctk.CTkLabel(self, wraplength=250)
        self.descripcion_label.pack_configure(**self.default_padding)
        self.descripcion_label.pack()

        frame_info_evento = ctk.CTkFrame(self, fg_color="transparent")
        frame_info_evento.pack_configure(fill="both", expand=True)
        frame_info_evento.pack()

        self.info_evento_label = ctk.CTkLabel(frame_info_evento)
        self.info_evento_label.pack_configure(side="bottom", **self.default_padding)
        self.info_evento_label.pack()

        frame_principal_direccion = ctk.CTkFrame(self, fg_color="transparent")
        frame_principal_direccion.pack_configure(fill="both", expand=True)
        frame_principal_direccion.pack()

        frame_direccion = ctk.CTkFrame(frame_principal_direccion, fg_color="transparent")
        frame_direccion.pack_configure(side="bottom", **self.default_padding)
        frame_direccion.pack()

        nombre_ubicacion_fuente = ctk.CTkFont(weight="bold")
        self.nombre_ubicacion_label = ctk.CTkLabel(frame_direccion, font=nombre_ubicacion_fuente)
        self.nombre_ubicacion_label.pack()

        self.direccion_ubicacion_label = ctk.CTkLabel(frame_direccion)
        self.direccion_ubicacion_label.pack()

        boton_ver_mapa = ctk.CTkButton(frame_direccion, text="Ver en mapa", command=self.ir_a_mapa, **self.default_button_color)
        boton_ver_mapa.pack_configure(**self.default_padding)
        boton_ver_mapa.pack()

        self.master.bind("<<inicializar_proximos>>", self._inicializar)
        
        self.boton_atras.pack_configure(side='bottom', **self.default_padding)
        self.boton_atras.pack()

    def _establecer_info_evento(self):
        evento = self.controlador.obtener_evento_actual()
        ubicacion = self.controlador.obtener_ubicacion_actual()
        self.titulo_label.configure(text=evento.nombre)
        self.descripcion_label.configure(text=evento.descripcion)
        self.nombre_ubicacion_label.configure(text=ubicacion.nombre)
        self.direccion_ubicacion_label.configure(text=ubicacion.direccion)
        (fecha, hora_inicio) = evento.hora_inicio.split("T")
        info = f"Artista: {evento.artista}\nGenero: {evento.genero}\nFecha: {fecha} {hora_inicio}"
        self.info_evento_label.configure(text=info)

    def _inicializar(self, *args):
        self._establecer_info_evento()
    
    # Navegacion

    def ir_a_mapa(self):
        self.controlador.ir_a_mapa()