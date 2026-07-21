from docx import Document


def leer_word(ruta):

    doc = Document(ruta)

    texto = []

    for p in doc.paragraphs:

        if p.text.strip() != "":
            texto.append(p.text.strip())

    return "\n".join(texto)