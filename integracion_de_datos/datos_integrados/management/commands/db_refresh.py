from django.core.management.base import BaseCommand
from .utils.scrapper import scrape_property_data
from .meli_request import get_new_properties_meli
from datos_integrados.models import Property
from .utils.encontrar_primer_numero import encontrar_primer_numero
from .utils.calcular_similitud_palabras import calcular_similitud

def get_new_properties_gallito():
    TEST_GALLITO_URL = 'https://www.gallito.com.uy/apto-al-frente-casi-imm-2-dormitorios-tza-con-cerramiento-inmuebles-24375924'
    # Toma 10 veces la misma url, tendria que tomar los nuevos inmuebles, a mejorar
    urls_array = [TEST_GALLITO_URL for _ in range(10)]
    new_properties =  [scrape_property_data(url) for url in urls_array]
    for new_property in new_properties:
        new_property["tipo"] = new_property["tipo"].lower()
        new_property["barrio"] = new_property["barrio"].lower()
        new_property["cuartos"] = int(encontrar_primer_numero(new_property["cuartos"])) if new_property["cuartos"] is not None else None
        new_property["metros_cuadrados"] = int(encontrar_primer_numero(new_property["metros_cuadrados"])) if new_property["metros_cuadrados"] is not None else None
        new_property["precio"] = int(encontrar_primer_numero(new_property["precio"])) if new_property["precio"] is not None else None
        new_property["gastos_comunes"] = int(encontrar_primer_numero(new_property["gastos_comunes"])) if new_property["gastos_comunes"] is not None else None
    return new_properties

def is_property_in_database(new_property):
    """ !!! Falta implementar !!!
    Es la funcion encargada de resolver los conflictos cuando ya existe en la base la propiedad """
    properties = Property.objects.values_list('titulo', flat=True)
    for property_titulo in properties:
        if calcular_similitud(new_property["titulo"].lower(), property_titulo.lower()) > 0.8:
            return True        
    return False

def load_new_properties(properties):
    """Se encarga de resolver los conflictos de inmuebles repetidos y persistirlos en la base
    Toma un objeto con las mismas propiedades que el modelo Property"""
    for property in properties:
        # actualizar por checkeo si realmente existe o no
        already_exists = is_property_in_database(property)
        if not already_exists:
            Property(
                titulo=property["titulo"],
                tipo=property["tipo"],
                cuartos=property["cuartos"],
                metros_cuadrados=property["metros_cuadrados"],
                barrio=property["barrio"],
                precio=property["precio"],
                gastos_comunes=property["gastos_comunes"],
                direccion=property["direccion"],
                url=property["url"]
            ).save()

class Command(BaseCommand):
    """Obtiene los inmuebles de Mercadolibre y el gallito y los carga.
    En caso de que el inmueble ya exista en la base,
    resuelve si quedarse con lo que esta en la base o el inmueble nuevo"""

    def handle(self, *args, **kwargs):
        meli_properties = get_new_properties_meli()
        load_new_properties(meli_properties)
        # gallito_properties = get_new_properties_gallito()
        # load_new_properties(gallito_properties)
        