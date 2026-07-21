import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUTA_PROMPT = os.path.join(
    BASE_DIR,
    "Prompts",
    "prompt_cuestionario.txt"
)
def crear_prompt_cuestionario(ruta_json):
    with open(ruta_json,"r",encoding="utf-8") as f:
        datos=json.load(f)
    texto_json=json.dumps(
        datos,
        indent=4,
        ensure_ascii=False
    )
    with open(RUTA_PROMPT,"r",encoding="utf-8") as f:
        plantilla=f.read()
    
    prompt=plantilla.replace("{json}",texto_json)
    return prompt
