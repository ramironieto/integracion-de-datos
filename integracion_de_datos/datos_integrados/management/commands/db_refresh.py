from django.core.management.base import BaseCommand

def get_new_data_meli():
    pass

def get_new_data_gallito():
    pass

def load_new_properties(properties)
    """Se encarga de resolver los conflictos de inmuebles repetidos y persistirlos en la base"""
    pass


class Command(BaseCommand):
    """obtiene data de Mercadolibre y la carga, """

    def handle(self, *args, **kwargs):
        meli_properties = get_new_data_meli()
        load_new_properties(meli_properties)
        gallito_properties = get_new_data_gallito()
        load_new_properties(gallito_properties)
        