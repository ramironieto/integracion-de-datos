from django.core.management.base import BaseCommand
from .utils.scrapper import scrape_property_data
from .meli_request import get_new_properties_meli
from datos_integrados.models import Property
from .utils.encontrar_primer_numero import encontrar_primer_numero
from .utils.calcular_similitud_palabras import calcular_similitud
from django.core import serializers

def get_new_properties_gallito():
    TEST_GALLITO_URL = [
        'https://www.gallito.com.uy/apto-al-frente-casi-imm-2-dormitorios-tza-con-cerramiento-inmuebles-24375924',
        'https://www.gallito.com.uy/proximo-rambla-y-montevideo-shopping-inmuebles-24638458',
        'https://www.gallito.com.uy/alquiler-apartamento-monoambiente-puerto-buceo-kaiken-202-s-inmuebles-24668010',
        'https://www.gallito.com.uy/alquiler-apto-1-dormitorio-buceo-inmuebles-24486760',
        'https://www.gallito.com.uy/alquila-hermoso-monoambiente-con-patio-inmuebles-23639689',
        'https://www.gallito.com.uy/apartamento-en-alquiler-monoambiente-1-ba%C3%A3%C2%B1o-amplio-pa-inmuebles-24344800',
        'https://www.gallito.com.uy/alquiler-monoambiente-planta-baja-patio-buceo-inmuebles-24467241',
        'https://www.gallito.com.uy/alquilo-lofts-a-estrenar-zona-buceo-wtc-inmuebles-24541288',
        'https://www.gallito.com.uy/fco-anzani-y-rivera-inmuebles-24654300',
        'https://www.gallito.com.uy/alquiler-monoambiente-premium-zona-wtc-buceo-cpatio-y-inmuebles-24674320',
    ]
    # Toma 10 veces la misma url, tendria que tomar los nuevos inmuebles, a mejorar
    new_properties =  [scrape_property_data(url) for url in TEST_GALLITO_URL]

    for new_property in new_properties:
        numero_cuartos = encontrar_primer_numero(new_property["cuartos"])

        new_property["tipo"] = new_property["tipo"].lower()
        new_property["barrio"] = new_property["barrio"].lower()
        new_property["cuartos"] = int(numero_cuartos) if numero_cuartos is not None else None
        new_property["metros_cuadrados"] = int(encontrar_primer_numero(new_property["metros_cuadrados"])) if new_property["metros_cuadrados"] is not None else None
        new_property["precio"] = int(encontrar_primer_numero(new_property["precio"])) if new_property["precio"] is not None else None
        new_property["gastos_comunes"] = int(encontrar_primer_numero(new_property["gastos_comunes"])) if new_property["gastos_comunes"] is not None else None
    return new_properties

def is_property_in_database(new_property):
    """ !!! Falta implementar !!!
    Es la funcion encargada de resolver los conflictos cuando ya existe en la base la propiedad """
    properties = Property.objects.all()
    for property in properties:
        if calcular_similitud(new_property["titulo"].lower(), property.titulo.lower()) > 0.9:
            return property.id       
    return False

def load_new_properties(properties):
    """Se encarga de resolver los conflictos de inmuebles repetidos y persistirlos en la base
    Toma un objeto con las mismas propiedades que el modelo Property"""
    for property in properties:
        # actualizar por checkeo si realmente existe o no
        already_exists_id = is_property_in_database(property)
        if not already_exists_id:
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
        else:
            property_old = Property.objects.get(id=already_exists_id)
            print(f"PROPIEDAD REPETIDA ENCONTRADA: Actual: {property_old.titulo} - Candidata: {property['titulo']}")
            cantidad_none_new = sum(valor is None for valor in property.values())
            cantidad_none_old = sum(getattr(property_old, campo.name) is None for campo in Property._meta.get_fields())
            print(f"Cantidad de valores nulos actual: {cantidad_none_old}")
            print(f"Cantidad de valores nulos candidata: {cantidad_none_new}")
            if cantidad_none_new < cantidad_none_old:
                print(f"Deleting {property_old.titulo}")
                property_old.delete()
                print(f"Creating {property['titulo']}")
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
        gallito_properties = get_new_properties_gallito()
        load_new_properties(gallito_properties)
        meli_properties = get_new_properties_meli()
        load_new_properties(meli_properties)
        