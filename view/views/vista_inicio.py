from view.vista_principal import VistaPrincipal

import customtkinter as ctk


class VistaInicio(VistaPrincipal):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.configure(text="Tour Musical")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        fuente_descripcion = ctk.CTkFont(size=12)
        descripcion = ctk.CTkLabel(self, text="Descubre eventos musicales, planifica rutas y comparte tu experiencia de manera eficiente y agradable con esta app", font=fuente_descripcion, wraplength=250)
        descripcion.pack(padx=10, pady=15)

        frame_navegacion = ctk.CTkFrame(self, fg_color="transparent")

        boton_explorar = ctk.CTkButton(frame_navegacion, text="Explorar eventos", command=self.ir_a_explorar, **self.default_button_color)
        boton_explorar.grid(row=0, column=0, **self.default_padding)

        boton_buscar = ctk.CTkButton(frame_navegacion, text="Buscar eventos", command=self.ir_a_busqueda, **self.default_button_color)
        boton_buscar.grid(row=1, column=0, **self.default_padding)

        boton_asistidos = ctk.CTkButton(frame_navegacion, text="Eventos asistidos", command=self.ir_a_asistidos, **self.default_button_color)
        boton_asistidos.grid(row=2, column=0, **self.default_padding)

        frame_navegacion.pack(padx=10, pady=15)

        frame_opciones = ctk.CTkFrame(self, fg_color="transparent")

        boton_ajustes = ctk.CTkButton(frame_opciones, text="Ajustes", **self.default_button_color, command=self.ir_a_ajustes)
        boton_ajustes.pack_configure(side='left', **self.default_padding)
        boton_ajustes.pack()

        boton_salir = ctk.CTkButton(frame_opciones, text="Salir", **self.default_button_color, command=self.master.destroy)
        boton_salir.pack_configure(side='right', **self.default_padding)
        boton_salir.pack()

        frame_opciones.pack_configure(side="bottom", **self.default_padding)
        frame_opciones.pack()

    def ir_a_ajustes(self):
        self.controlador.ir_a_ajustes()

    def ir_a_explorar(self):
        self.controlador.ir_a_explorar()

    def ir_a_busqueda(self):
        self.controlador.ir_a_busqueda()

    def ir_a_asistidos(self):
        self.controlador.ir_a_asistidos()