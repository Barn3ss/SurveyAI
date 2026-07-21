import customtkinter as ctk

from UI.styles import *


class ConfigPanel(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            corner_radius=CORNER_RADIUS
        )

        self.pack(fill="x", padx=25, pady=10)

        ctk.CTkLabel(
            self,
            text="⚙ Configuración",
            font=SECTION_FONT
        ).pack(anchor="w", padx=15, pady=(10,15))

        self.numero = ctk.CTkComboBox(
            self,
            values=[str(i) for i in range(1,11)],
            width=120
        )

        self.numero.set("1")

        self.numero.pack(
            padx=15,
            pady=(0,15),
            anchor="w"
        )
        