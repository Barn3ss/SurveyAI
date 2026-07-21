from google import genai
from config import API_KEY, MODELO
import json

client=genai.Client(api_key=API_KEY)

def llamar_ia(prompt, tipo="texto"):
    print("-------------------------")
    print("Enviando prompt a la IA...")
    print("-------------------------")

    respuesta=client.models.generate_content(
        model=MODELO,
        contents=prompt
    )
    if tipo=="json":
        texto=respuesta.text.strip()
        if texto.startswith("''''json"):
            texto=texto.replace("''''json","",1)
        if texto.endswith("''''"):
            texto=texto[:-3]
        texto=texto.strip()
        return json.loads(texto)
    return respuesta.text

