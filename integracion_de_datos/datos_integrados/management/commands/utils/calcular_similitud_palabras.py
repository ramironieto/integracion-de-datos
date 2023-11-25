from difflib import SequenceMatcher

def calcular_similitud(texto1, texto2):
    # Crear un objeto SequenceMatcher
    comparador = SequenceMatcher(None, texto1, texto2)

    # Obtener la proporción de similitud
    similitud = comparador.ratio()

    return similitud