import os
from Modules.leer_word import leer_word
from Modules.limpiar_texto import limpiar_texto
from Modules.crear_prompt import crear_prompt
from Modules.llamar_IA import llamar_ia
from Modules.guardar_json import guardar_json
from Modules.obtener_nombre_proyecto import obtener_nombre_proyecto
from Modules.crear_proyectos import crear_proyecto
from Modules.crear_cuestionario import crear_cuestionario
from Modules.obtener_version import obtener_version
import shutil

def generar_prompt(ruta_briefing,base_dir,numero_cuestionarios=1):

    texto = leer_word(ruta_briefing)

    texto = limpiar_texto(texto)

    prompt = crear_prompt(texto)

 
    respuesta=llamar_ia(prompt,tipo="json")
    nombre_proyecto=obtener_nombre_proyecto(respuesta)
    ruta_proyecto=crear_proyecto(nombre_proyecto,base_dir)
    version=obtener_version(
        os.path.join(ruta_proyecto,"Analisis"),
        "prompt",
        ".txt"
    )
    ruta_prompt=os.path.join(
        ruta_proyecto,
        "Analisis",
        f"prompt_v{version}.txt"
    )
    ruta_json=os.path.join(
        ruta_proyecto,
        "Analisis",
        "briefing_v1.json"
    )
    ruta_word=os.path.join(
        ruta_proyecto,
        "Briefing",
        os.path.basename(ruta_briefing)
    )
    #copiar el briefing
    shutil.copy2(ruta_briefing, ruta_word)
    #guardar prompt
    print("----PROMPT----")
    print(prompt)
    print("------------------")
    with open(ruta_prompt,"w",encoding="utf_8") as f:
        f.write(prompt)
    #guardar JSON
    guardar_json(respuesta,ruta_json)
    for _ in range(numero_cuestionarios):
        crear_cuestionario(
            ruta_json,
            ruta_proyecto
        ) 
    print(f"Proyecto creado en :{ruta_proyecto}")
    return ruta_proyecto     
    
