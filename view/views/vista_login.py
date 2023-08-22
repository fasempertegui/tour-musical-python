from view.vista_principal import VistaPrincipal

import customtkinter as ctk


class VistaLogin(VistaPrincipal):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label.configure(text="Iniciar sesion")
        self.titulo_label.pack_configure(side="top", **self.default_padding)
        self.titulo_label.pack()

        self.nombre_usuario_label = ctk.CTkLabel(self, text="Nombre de usuario")
        self.nombre_usuario_label.pack()

        self.nombre_usuario_entry = ctk.CTkEntry(self)
        self.nombre_usuario_entry.pack_configure(**self.default_padding)
        self.nombre_usuario_entry.pack()

        self.contrasena_label = ctk.CTkLabel(self, text="Contraseña")
        self.contrasena_label.pack()
        
        self.contrasena_entry = ctk.CTkEntry(self, show="*")
        self.contrasena_entry.pack_configure(**self.default_padding)
        self.contrasena_entry.pack()

        frame_botones = ctk.CTkFrame(self, fg_color="transparent")
        frame_botones.pack_configure(**self.default_padding)
        frame_botones.pack()

        self.boton_login = ctk.CTkButton(frame_botones, text="Iniciar sesión", command=self._login, **self.default_button_color)
        self.boton_login.pack_configure(side="left", padx=3, pady=3)
        self.boton_login.pack()

        self.boton_registro = ctk.CTkButton(frame_botones, text="Registrarse", command=self._registrar, **self.default_button_color)
        self.boton_registro.pack_configure(side="right", padx=3, pady=3)
        self.boton_registro.pack()

    def _login(self, *args):
        username = self.nombre_usuario_entry.get()
        password = self.contrasena_entry.get()
        if self.controlador.autenticar(username, password):
            self.controlador.ir_a_inicio()
        else:
            print("Inicio de sesión fallido")

    def _registrar(self, *args):
        pass