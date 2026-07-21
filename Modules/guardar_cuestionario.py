def guardar_cuestionario(cuestionario, ruta_salida):

    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(cuestionario)

    return ruta_salida