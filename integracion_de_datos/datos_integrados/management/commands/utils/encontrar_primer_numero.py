import re


def encontrar_primer_numero(texto):
    # Utilizamos una expresión regular para buscar números, ya sean enteros o decimales
    patron = re.compile(r'\d+(\.\d+)?')
    
    # Buscamos el patrón en el texto
    coincidencia = patron.search(texto)
    
    # Verificamos si se encontró alguna coincidencia
    if coincidencia:
        # Devolvemos el número encontrado
            return coincidencia.group().replace(".", "")
    else:
        # En caso de no encontrar ningún número, devolvemos None
        return None