import json

def guardar_json(respuesta,ruta):
    datos=json.loads(respuesta)
    with open(ruta,"w",encoding="utf-8") as f:
        json.dump(datos,f,ensure_ascii=False,indent=4)
        