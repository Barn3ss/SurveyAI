import customtkinter as ctk

from UI.styles import *


class BriefingPanel(ctk.CTkFrame):

    def __init__(self, master, seleccionar_callback):

        super().__init__(
            master,
            corner_radius=CORNER_RADIUS
        )

        self.pack(fill="x", padx=25, pady=10)

        ctk.CTkLabel(
            self,
            text="📄 Briefing",
            font=SECTION_FONT
        ).pack(anchor="w", padx=15, pady=(10,5))

        self.archivo_label = ctk.CTkLabel(
            self,
            text="⚠ Ningún briefing seleccionado",
            font=TEXT_FONT
        )

        self.archivo_label.pack(
            anchor="w",
            padx=15,
            pady=(0,15)
        )

        self.boton = ctk.CTkButton(
            self,
            text="📂 Seleccionar briefing",
            command=seleccionar_callback,
            height=40
        )

        self.boton.pack(
            padx=15,
            pady=(0,15)
        )
    def actualizar_archivo(self, nombre):

        self.archivo_label.configure(
            text=f"Briefing seleccionado:\n{nombre}"
        )
        