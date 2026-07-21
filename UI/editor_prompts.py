import os
import shutil
import customtkinter as ctk
from UI.dialogs import confirmar, info

class PromptEditor(ctk.CTkToplevel):
    def __init__(self,master,base_dir):
        super().__init__(master)
        self.base_dir=base_dir
        self.title("Editor de prompts")
        self.geometry("350x220")
        self.resizable(False,False)
        ctk.CTkButton(
            self,
            text="Editar prompt briefing",
            command=self.editar_prompt_briefing
        ).pack(pady=10)
        
        ctk.CTkButton(
            self,
            text="Editar prompt cuestionario",
            command=self.editar_prompt_cuestionario
        ).pack(pady=10)
        
        ctk.CTkButton(
            self,
            text="Restaurar prompts originales",
            command=self.restaurar_prompts
        ).pack(pady=10)
    def editar_prompt_briefing(self):
        if not confirmar(
            "Editar prompt",
            "Los cambios afectarán a todos los proyectos futuros.\n\n¿Continuar?"
        ):
            return
        os.startfile(
            os.path.join(
                self.base_dir,
                "Prompts",
                "Prompt_briefing.txt"
            )
        )
    def editar_prompt_cuestionario(self):
        if not confirmar(
            "Editar prompt",
            "Los cambios afectarán a todos los proyectos futuros.\n\n¿Continuar?"
        ):
            return
        os.startfile(
            os.path.join(
                self.base_dir,
                "Prompts",
                "Prompt_cuestionario.txt"
            )
        )
    def restaurar_prompts(self):
        if not confirmar(
            "Restaurar",
            "Se restaurarán los prompts originales.\n\n¿Continuar?"
        ):
            return
        shutil.copy2(
            os.path.join(
                self.base_dir,
                "Prompts_default",
                "prompt_briefing.txt"
            ),
            os.path.join(
                self.base_dir,
                "Prompts",
                "prompt_briefing.txt"
            )
        )
        shutil.copy2(
            os.path.join(
                self.base_dir,
                "Prompts_default",
                "prompt_cuestionario.txt"
            ),
            os.path.join(
                self.base_dir,
                "Prompts",
                "prompt_cuestionario.txt"
            )
        )

        info(
            "SurveyAI",
            "Prompts restaurados correctamente"
        )
