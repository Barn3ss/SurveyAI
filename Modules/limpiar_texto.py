import re


def limpiar_texto(texto):

    lineas = []

    for linea in texto.splitlines():

        linea = linea.strip()

        if linea:
            lineas.append(linea)

    return "\n".join(lineas)