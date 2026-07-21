
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUTA_PROMPT = os.path.join(
    BASE_DIR,
    "Prompts",
    "prompt_briefing.txt"
)


def crear_prompt(briefing):

    with open(RUTA_PROMPT, "r", encoding="utf-8") as f:
        plantilla = f.read()

    prompt = plantilla.replace("{briefing}", briefing)

    return prompt


