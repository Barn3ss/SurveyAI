from UI.components.briefing_panel import BriefingPanel
from UI.components.status_panel import StatusPanel
from UI.components.config_panel import ConfigPanel
from UI.components.action_buttons import ActionButtons
from UI.components.footer import Footer
from UI.editor_prompts import PromptEditor
from UI.styles import *
from tkinter import messagebox, filedialog
import customtkinter as ctk
import os
from Modules.generar_prompt import generar_prompt

class SurveyAI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.BASE_DIR=os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
        self.ruta_briefing=None
        self.title("SurveyAI")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False,False)
        self.crear_interfaz()
    def crear_interfaz(self):

        self.titulo = ctk.CTkLabel(
            self,
            text="🤖 SurveyAI",
            font=TITLE_FONT
        )   
        self.titulo.pack(pady=(25,5))

        self.subtitulo = ctk.CTkLabel(
            self,
            text="AI Survey Generator",
            font=SUBTITLE_FONT
        )
        self.subtitulo.pack(pady=(0,20))

        self.briefing = BriefingPanel(
            self,
            self.seleccionador_archivo
        )

        self.status = StatusPanel(self)

        self.config = ConfigPanel(self)

        self.buttons = ActionButtons(
            self,
            self.generar,
            lambda: PromptEditor(self, self.BASE_DIR)
        )

        self.footer = Footer(self)
    

    def seleccionador_archivo(self):
        archivo=filedialog.askopenfilename(
            title="Selecciona el briefing",
            filetypes=[("Documentos Word","*.docx")]
        )   
        if archivo:
            self.ruta_briefing=archivo
            self.actualizar_archivo(archivo)
            self.actualizar_estado("Listo para generar")
            self.actualizar_progreso(0)
    def actualizar_estado(self, texto):
        self.status.actualizar_estado(texto)
        self.update_idletasks()
    def actualizar_progreso(self, valor):
        self.status.actualizar_progreso(valor)
        self.update_idletasks()
    def actualizar_archivo(self, ruta):
        nombre = os.path.basename(ruta)
        self.briefing.actualizar_archivo(nombre)
        self.update_idletasks()
   
   
    def generar(self):
        self.buttons.boton_generar.configure(state="disabled")
        try:
            self.actualizar_progreso(0)
            if self.ruta_briefing is None:
                messagebox.showwarning(
                    "Briefing no seleccionado",
                    "Antes de generar la encuesta debes selecconar un briefing."
                )
                self.actualizar_estado("Esperando briefing...")
                self.buttons.boton_generar.configure(state="normal")
                return
            
            self.actualizar_estado("Leyendo briefing...")
            self.actualizar_progreso(20)
    
            ruta_proyecto=generar_prompt(self.ruta_briefing,self.BASE_DIR,self.config.numero.get())
            self.actualizar_estado(
                f"Proyecto creado:{os.path.basename(ruta_proyecto)}"
                )
            self.actualizar_progreso(100)
        finally:
            self.buttons.boton_generar.configure(state="normal")

