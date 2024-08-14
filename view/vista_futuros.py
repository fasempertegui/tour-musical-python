from utils.utils_vista import VistaUtils

import customtkinter as ctk


class VistaFuturos(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="")
        self.titulo_label.pack()

        self.descripcion_label = ctk.CTkLabel(self, wraplength=250)
        self.descripcion_label.pack_configure(**VistaUtils.padding)
        self.descripcion_label.pack()

        frame_info_evento = ctk.CTkFrame(self, fg_color="transparent")
        frame_info_evento.pack_configure(fill="both", expand=True)
        frame_info_evento.pack()

        self.info_evento_label = ctk.CTkLabel(frame_info_evento)
        self.info_evento_label.pack_configure(side="bottom", **VistaUtils.padding)
        self.info_evento_label.pack()

        frame_principal_direccion = ctk.CTkFrame(self, fg_color="transparent")
        frame_principal_direccion.pack_configure(fill="both", expand=True)
        frame_principal_direccion.pack()

        frame_direccion = ctk.CTkFrame(frame_principal_direccion, fg_color="transparent")
        frame_direccion.pack_configure(side="bottom", **VistaUtils.padding)
        frame_direccion.pack()

        nombre_ubicacion_fuente = ctk.CTkFont(weight="bold")
        self.nombre_ubicacion_label = ctk.CTkLabel(frame_direccion, font=nombre_ubicacion_fuente)
        self.nombre_ubicacion_label.pack()

        self.direccion_ubicacion_label = ctk.CTkLabel(frame_direccion)
        self.direccion_ubicacion_label.pack()

        boton_ver_mapa = ctk.CTkButton(frame_direccion, text="Ver en mapa", command=self._ir_a_mapa, **VistaUtils.estilo_boton)
        boton_ver_mapa.pack_configure(**VistaUtils.padding)
        boton_ver_mapa.pack()

        self._inicializar()

        self.boton_atras = VistaUtils.crear_boton_atras(self)
        self.boton_atras.configure(command=self._regresar)
        self.boton_atras.pack()

    # Privados

    def _inicializar(self, *args):
        evento = self.controlador.obtener_evento_actual()
        ubicacion = self.controlador.obtener_ubicacion_actual()
        self.titulo_label.configure(text=evento.nombre)
        self.descripcion_label.configure(text=evento.descripcion)
        self.nombre_ubicacion_label.configure(text=ubicacion.nombre)
        self.direccion_ubicacion_label.configure(text=ubicacion.direccion)
        fecha = evento.hora_inicio.date().strftime("%d-%m-%Y")
        hora_inicio = evento.hora_inicio.time().strftime("%H:%M:%S")
        info = f"Artista: {evento.artista}\nGenero: {evento.genero}\nFecha: {fecha} {hora_inicio}"
        self.info_evento_label.configure(text=info)

    # Navegacion

    def _ir_a_mapa(self):
        self.controlador.ir_a_mapa()

    def _regresar(self):
        self.controlador.regresar()
