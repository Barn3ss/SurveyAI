import json


def obtener_nombre_proyecto(datos):

    cliente = datos.get("cliente", "Cliente")
    metodologia = datos.get("metodologia", "Proyecto")
    pais=datos.get("pais","Pais")

    if pais in ("","No especificado"):
        nombre_proyecto=f"{cliente}_{metodologia}"
    else:
        nombre_proyecto=f"{cliente}_{metodologia}_{pais}"

    # Limpiar caracteres problemáticos
    nombre_proyecto = nombre_proyecto.replace(" ", "_")
    nombre_proyecto = nombre_proyecto.replace("/", "-")
    nombre_proyecto = nombre_proyecto.replace("\\", "-")
    nombre_proyecto = nombre_proyecto.replace(":", "")
    nombre_proyecto = nombre_proyecto.replace("*", "")
    nombre_proyecto = nombre_proyecto.replace("?", "")
    nombre_proyecto = nombre_proyecto.replace('"', "")
    nombre_proyecto = nombre_proyecto.replace("<", "")
    nombre_proyecto = nombre_proyecto.replace(">", "")
    nombre_proyecto = nombre_proyecto.replace("|", "")
    nombre_proyecto=nombre_proyecto.replace("'","")

    return nombre_proyecto

