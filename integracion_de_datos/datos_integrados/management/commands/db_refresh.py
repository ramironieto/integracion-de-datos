from django.core.management.base import BaseCommand
from .utils.scrapper import scrape_property_data
from .meli_request import get_new_properties_meli

def get_new_properties_gallito():
    TEST_GALLITO_URL = 'https://www.gallito.com.uy/apto-al-frente-casi-imm-2-dormitorios-tza-con-cerramiento-inmuebles-24375924'
    # Toma 10 veces la misma url, tendria que tomar los nuevos inmuebles, a mejorar
    urls_array = [TEST_GALLITO_URL for _ in range(10)]
    new_properties =  [scrape_property_data(url) for url in urls_array]
    return new_properties

def is_property_in_database(property):
    """ !!! Falta implementar !!!
    Es la funcion encargada de resolver los conflictos cuando ya existe en la base la propiedad """
    return False

def load_new_properties(properties):
    """Se encarga de resolver los conflictos de inmuebles repetidos y persistirlos en la base
    Toma un objeto con las mismas propiedades que el modelo Property"""
    for property in properties:
        # actualizar por checkeo si realmente existe o no
        already_exists = is_property_in_database(property)
        if not already_exists:
            print("Nuevo inmueble!")
            # crear nueva instancia de inmueble

class Command(BaseCommand):
    """Obtiene los inmuebles de Mercadolibre y el gallito y los carga.
    En caso de que el inmueble ya exista en la base,
    resuelve si quedarse con lo que esta en la base o el inmueble nuevo"""

    def handle(self, *args, **kwargs):
        meli_properties = get_new_properties_meli()
        load_new_properties(meli_properties)
        gallito_properties = get_new_properties_gallito()
        load_new_properties(gallito_properties)
        