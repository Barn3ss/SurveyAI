import os
import re

def obtener_version(carpeta,prefijo,extension):
    mayor_version=0
    for archivo in os.listdir(carpeta):
        patron=rf"{prefijo}_v(\d+){re.escape(extension)}"
        coincidencia=re.fullmatch(patron,archivo)

        if coincidencia:
            version=int(coincidencia.group(1))
            if version > mayor_version:
                mayor_version=version
    return mayor_version+1
