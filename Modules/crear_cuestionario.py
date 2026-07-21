import os 
from Modules.crear_prompt_cuestionario import crear_prompt_cuestionario
from Modules.llamar_IA import llamar_ia
from Modules.guardar_cuestionario import guardar_cuestionario
from Modules.exportar_cuestionario_docx import exportar_cuestionario_docx
from Modules.obtener_version import obtener_version

def crear_cuestionario(ruta_json,ruta_proyecto):
    prompt= crear_prompt_cuestionario(ruta_json)
    respuesta=llamar_ia(prompt,tipo="texto")
    version=obtener_version(
        os.path.join(ruta_proyecto,"Cuestionarios"),
        "cuestionario",
        ".md"
    )

    ruta_cuestionario= os.path.join(ruta_proyecto, "Cuestionarios",f"cuestionario_v{version}.md")
    guardar_cuestionario(respuesta,ruta_cuestionario)
    ruta_docx=os.path.join(
        ruta_proyecto,
        "Cuestionarios",
        f"cuestionario_v{version}.docx"
    )
    exportar_cuestionario_docx(
        ruta_cuestionario,
        ruta_docx
    )
    return ruta_cuestionario

