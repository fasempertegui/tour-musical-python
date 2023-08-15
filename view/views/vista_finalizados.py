from view.vista_principal import VistaPrincipal

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaFinalizados(VistaPrincipal):
    def __init__(self, master=None, controlador=None):
        super().__init__(master, controlador)

        self.titulo_label.pack(**self.default_padding)

        descripcion_fuente = Font(size=10)
        self.descripcion_label = ttk.Label(
            self, font=descripcion_fuente, wraplength=250
        )
        self.descripcion_label.pack(**self.default_padding)

        self.info_evento_label = ttk.Label(self)
        self.info_evento_label.pack(**self.default_padding)

        frame_reviews = ttk.Frame(self)

        estado_fuente = Font(size=9, weight="bold")
        estado_label = ttk.Label(
            self, text="Evento finalizado", font=estado_fuente)
        estado_label.pack(**self.default_padding)

        self.boton_confirmar_asistencia = ttk.Button(
            frame_reviews, command=self.confirmar_asistencia)
        self.boton_confirmar_asistencia.pack(side="top")

        self.boton_ver_reviews = ttk.Button(
            frame_reviews, text="Ver reviews", command=self.ir_a_reviews
        )
        self.boton_ver_reviews.pack(side="left")

        self.boton_escribir_review = ttk.Button(
            frame_reviews, text="Opinar", command=self.ir_a_escribir_review
        )
        self.boton_escribir_review.pack(side="right")

        frame_reviews.pack()

        self.master.bind("<<VistaFinalizados>>", self._inicializar)
        self.master.bind("<<Asistencia>>", self._inicializar)

        self.boton_atras.pack(side="bottom", **self.default_padding)

    def _determinar_usuario_puede_opinar(self, asistio):
        if self.controlador.determinar_usuario_puede_opinar(asistio):
            self.boton_escribir_review.configure(state="normal")
        else:
            self.boton_escribir_review.configure(state="disabled")

    def _determinar_usuario_asistio(self, *args):
        if self.controlador.determinar_usuario_asistio():
            self.boton_confirmar_asistencia.configure(state="disabled")
            self.boton_confirmar_asistencia["text"] = "Marcado como asistido"
            return True
        else:
            self.boton_confirmar_asistencia.configure(state="normal")
            self.boton_confirmar_asistencia["text"] = "Marcar como asistido"
            return False

    def _establecer_info_evento(self):
        evento = self.controlador.obtener_evento_actual()
        self.titulo_label["text"] = evento.nombre
        self.descripcion_label["text"] = evento.descripcion
        (fecha, hora_inicio) = evento.hora_inicio.split("T")
        info = f"Artista: {evento.artista}\nGenero: {evento.genero}\nFecha: {fecha} {hora_inicio}"
        self.info_evento_label["text"] = info

    def _inicializar(self, *args):
        self._establecer_info_evento()
        asistio = self._determinar_usuario_asistio()
        self._determinar_usuario_puede_opinar(asistio)

    def confirmar_asistencia(self, *args):
        self.controlador.confirmar_asistencia()

    # Navegacion

    def ir_a_reviews(self):
        self.controlador.ir_a_reviews()

    def ir_a_escribir_review(self):
        self.controlador.ir_a_escribir_review()
