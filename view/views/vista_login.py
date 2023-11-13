from view.vista_principal import VistaPrincipal

import tkinter as tk
import customtkinter as ctk


class VistaLogin(VistaPrincipal):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.configure(text="Tour Musical")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        frame_principal = ctk.CTkFrame(self)
        frame_principal.pack_configure(padx=10, pady=10, expand=True, fill="both")
        frame_principal.pack()

        sesion_fuente = ctk.CTkFont(size=16, weight="bold")
        self.sesion_label = ctk.CTkLabel(frame_principal, font=sesion_fuente)
        self.sesion_label.configure(text="Iniciar sesion")
        self.sesion_label.pack_configure(**self.default_padding)
        self.sesion_label.pack()

        alerta_fuente = ctk.CTkFont(size=12)
        self.alerta_label = ctk.CTkLabel(frame_principal, font=alerta_fuente, text_color="red")

        datos_frame = ctk.CTkFrame(frame_principal, fg_color="transparent")
        datos_frame.rowconfigure(0, weight=1)
        datos_frame.columnconfigure(0, weight=1)
        datos_frame.pack()

        self.nombre_usuario_label = ctk.CTkLabel(datos_frame, text="Usuario")
        self.nombre_usuario_label.grid_configure(row=0, column=0, padx=5, pady=5)
        self.nombre_usuario_label.grid()

        self.nombre_usuario_entry = ctk.CTkEntry(datos_frame)
        self.nombre_usuario_entry.grid_configure(row=0, column=1, padx=5, pady=5)
        self.nombre_usuario_entry.grid()

        self.contrasena_label = ctk.CTkLabel(datos_frame, text="Contraseña")
        self.contrasena_label.grid_configure(row=1, column=0, padx=5, pady=5)
        self.contrasena_label.grid()

        self.contrasena_entry = ctk.CTkEntry(datos_frame, show="*")
        self.contrasena_entry.grid_configure(row=1, column=1, padx=5, pady=5)
        self.contrasena_entry.grid()

        frame_botones = ctk.CTkFrame(frame_principal, fg_color="transparent")
        frame_botones.rowconfigure(0, weight=1)
        frame_botones.columnconfigure(0, weight=1)
        frame_botones.pack()

        self.boton_login = ctk.CTkButton(frame_botones, text="Iniciar sesión", command=self._autenticar_usuario, **self.default_button_color)
        self.boton_login.grid_configure(row=0, column=0, padx=5, pady=10)
        self.boton_login.grid()

        self.boton_registro = ctk.CTkButton(frame_botones, text="Registrarse", command=self._registrar_usuario, **self.default_button_color)
        self.boton_registro.grid_configure(row=0, column=1, padx=5, pady=10)
        self.boton_registro.grid()

        self.master.bind("<<DatosInvalidos>>", self._datos_invalidos)
        self.master.bind("<<EnUso>>", self._en_uso)
        self.master.bind("<<CamposVacios>>", self._campos_vacios)


    def _autenticar_usuario(self, *args):
        username = self.nombre_usuario_entry.get()
        password = self.contrasena_entry.get()
        if self.controlador.autenticar_usuario(username, password):
            self.controlador.renderizar()

    def _registrar_usuario(self, *args):
        username = self.nombre_usuario_entry.get()
        password = self.contrasena_entry.get()
        if self.controlador.registrar_usuario(username, password):
            self.controlador.renderizar()

    def _datos_invalidos(self, *args):
        self.alerta_label.configure(text="Los datos ingresados no coinciden")
        self.alerta_label.pack()

    def _en_uso(self, *args):
        self.alerta_label.configure(text="Nombre de usuario en uso")
        self.alerta_label.pack()

    def _campos_vacios(self, *args):
        self.alerta_label.configure(text="Los campos no pueden estar vacios")
        self.alerta_label.pack()