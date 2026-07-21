import os
import json
from datetime import datetime

def crear_proyecto(nombre_proyecto,base_dir):
    carpeta=os.path.join(base_dir,"Proyectos",nombre_proyecto)
    os.makedirs(carpeta,exist_ok=True)
    os.makedirs(os.path.join(carpeta,"Briefing"),exist_ok=True)
    os.makedirs(os.path.join(carpeta,"Analisis"),exist_ok=True)
    os.makedirs(os.path.join(carpeta,"Cuestionarios"),exist_ok=True)
    os.makedirs(os.path.join(carpeta,"Traducciones"),exist_ok=True)
    metadata={
        "nombre_proyecto":nombre_proyecto,
        "fecha_creacion":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ultima_modificacion":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "version_actual":1,
        "estado":"En desarrollo"
    }
    ruta_metadata=os.path.join(carpeta,"metadata.json")
    with open(ruta_metadata,"w",encoding="utf-8") as f:
        json.dump(metadata,f,ensure_ascii=False,indent=4)

    return carpeta




