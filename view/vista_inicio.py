from utils.utils_vista import VistaUtils

import customtkinter as ctk


class VistaInicio(ctk.CTkFrame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.controlador = controlador

        self.titulo_label = VistaUtils.crear_titulo(self, texto_titulo="Tu ubicacion")
        self.titulo_label.pack()

        fuente_descripcion = ctk.CTkFont(size=12)
        descripcion = ctk.CTkLabel(
            self, text="Descubre eventos musicales, planifica rutas y comparte tu experiencia de manera eficiente y agradable con esta app",
            font=fuente_descripcion, wraplength=250)
        descripcion.pack(padx=10, pady=15)

        frame_navegacion = ctk.CTkFrame(self, fg_color="transparent")

        boton_explorar = ctk.CTkButton(frame_navegacion, text="Explorar eventos", command=self.ir_a_explorar, **VistaUtils.estilo_boton)
        boton_explorar.grid(row=0, column=0, **VistaUtils.padding)

        boton_buscar = ctk.CTkButton(frame_navegacion, text="Buscar eventos", command=self.ir_a_busqueda, **VistaUtils.estilo_boton)
        boton_buscar.grid(row=1, column=0, **VistaUtils.padding)

        boton_asistidos = ctk.CTkButton(frame_navegacion, text="Eventos asistidos", command=self.ir_a_asistidos, **VistaUtils.estilo_boton)
        boton_asistidos.grid(row=2, column=0, **VistaUtils.padding)

        frame_navegacion.pack(padx=10, pady=15)

        frame_opciones = ctk.CTkFrame(self, fg_color="transparent")

        boton_ajustes = ctk.CTkButton(frame_opciones, text="Ajustes", **VistaUtils.estilo_boton, command=self.ir_a_ajustes)
        boton_ajustes.pack_configure(side='left', **VistaUtils.padding)
        boton_ajustes.pack()

        boton_salir = ctk.CTkButton(frame_opciones, text="Cerrar sesion", **VistaUtils.estilo_boton, command=self.cerrar_sesion)
        boton_salir.pack_configure(side='right', **VistaUtils.padding)
        boton_salir.pack()

        frame_opciones.pack_configure(side="bottom", **VistaUtils.padding)
        frame_opciones.pack()

        fuente_sesion = ctk.CTkFont(size=12)
        self.sesion = ctk.CTkLabel(self, font=fuente_sesion, wraplength=250)
        self.sesion.pack_configure(side='bottom', **VistaUtils.padding)
        self.sesion.pack()

        self._establecer_nombre_usuario()

    def cerrar_sesion(self):
        self.controlador.cerrar_sesion()

    def ir_a_ajustes(self):
        self.controlador.ir_a_ajustes()

    def ir_a_explorar(self):
        self.controlador.ir_a_explorar()

    def ir_a_busqueda(self):
        self.controlador.ir_a_busqueda()

    def ir_a_asistidos(self):
        self.controlador.ir_a_asistidos()

    def _establecer_nombre_usuario(self, *args):
        nombre_usuario = self.controlador.obtener_nombre_usuario()
        self.sesion.configure(text=f"Has iniciado sesión como {nombre_usuario}")
