from view.views.vista_info_evento import VistaInfoEvento

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class VistaFinalizados(VistaInfoEvento):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.id_evento = 0

        frame_reviews = ttk.Frame(self)

        estado_fuente = Font(size=9, weight="bold")
        estado_label = ttk.Label(self, text="Evento finalizado", font=estado_fuente)
        estado_label.pack(**self.default_padding)

        self.boton_confirmar_asistencia = ttk.Button(frame_reviews)
        self.boton_confirmar_asistencia.pack(side='top')

        self.boton_ver_reviews = ttk.Button(frame_reviews, text="Ver reviews", command=self.ir_a_reviews)
        self.boton_ver_reviews.pack(side="left")

        self.boton_escribir_review = ttk.Button(frame_reviews, text="Opinar", command=self.ir_a_escribir_review)
        self.boton_escribir_review.pack(side="right")

        frame_reviews.pack()

        # Boton en la clase padre, padre
        self.boton_atras.pack(side='bottom', **self.default_padding)

    def _determinar_usuario_puede_opinar(self, asistio, evento):
        self.boton_escribir_review.configure(state="normal")
        if self.controlador.determinar_usuario_puede_opinar(asistio, evento):
            self.boton_escribir_review.configure(state="disabled")

    def _determinar_usuario_asistio(self, evento):
        self.boton_confirmar_asistencia.configure(state="normal")
        self.boton_confirmar_asistencia["text"] = "Marcar como asistido"
        if self.controlador.determinar_usuario_asistio(evento):
            self.boton_confirmar_asistencia.configure(state="disabled")
            self.boton_confirmar_asistencia["text"] = "Marcado como asistido"
            return True
        return False

    def _establecer_estado_botones(self, evento):
        asistio = self._determinar_usuario_asistio(evento)
        self._determinar_usuario_puede_opinar(asistio, evento)

    def _establecer_info_evento(self, evento):
        self.titulo_label["text"] = evento.nombre
        self.descripcion_label["text"] = evento.descripcion
        (fecha, hora_inicio) = evento.hora_inicio.split("T")
        info = f"Artista: {evento.artista}\nGenero: {evento.genero}\nFecha: {fecha} {hora_inicio}"
        self.info_evento_label["text"] = info

    def set_evento(self, evento):
        self._establecer_estado_botones(evento)
        self._establecer_info_evento(evento)

    def ir_a_reviews(self):
        self.controlador.ir_a_reviews()

    def ir_a_escribir_review(self):
        self.controlador.ir_a_escribir_review()