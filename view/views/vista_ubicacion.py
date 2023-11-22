from view.vista_principal import VistaPrincipal

from tkintermapview import TkinterMapView
import customtkinter as ctk

class VistaUbicacion(VistaPrincipal):
    def __init__(self, master=None, controlador=None):
        super().__init__(master, controlador)

        self.titulo_label.configure(text="Tu ubicacion")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        frame_principal = ctk.CTkFrame(self, fg_color="transparent")
        frame_principal.pack_configure(fill="both", expand=True)
        frame_principal.pack()

        label = ctk.CTkLabel(frame_principal, text="Clic derecho para establecer tu ubicacion")
        label.pack()

        self.mapa = TkinterMapView(frame_principal, corner_radius=0)
        self.mapa.pack(padx=10, pady=10, fill="both", expand=True)
        self.mapa.add_right_click_menu_command(label="Estoy aqui", command=self.anadir_marcador, pass_coords=True)
        self.mapa.set_position(-24.78076361883803, -65.415784358493)
        self.mapa.set_zoom(15)

        frame_botones = ctk.CTkFrame(frame_principal, fg_color="transparent")
        frame_botones.rowconfigure(0, weight=1)
        frame_botones.columnconfigure(0, weight=1)
        frame_botones.pack_configure(side='bottom')
        frame_botones.pack()

        boton_aceptar = ctk.CTkButton(frame_botones, text="Aceptar", command=self.guardar_cambios, **self.default_button_color)
        boton_aceptar.grid_configure(row=0, column=0, padx=5, pady=10)
        boton_aceptar.grid()

        boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", command=self.controlador.regresar, **self.default_button_color)
        boton_cancelar.grid_configure(row=0, column=1, padx=5, pady=10)
        boton_cancelar.grid()

    def anadir_marcador(self, coordenadas):
        self.coordenadas = coordenadas
        self.mapa.set_marker(coordenadas[0], coordenadas[1], text="Tu ubicacion")

    def guardar_cambios(self):
        self.controlador.guardar_cambios(self.coordenadas)
        self.controlador.regresar()