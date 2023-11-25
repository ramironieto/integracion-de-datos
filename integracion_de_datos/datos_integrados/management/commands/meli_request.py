from django.core.management.base import BaseCommand
import requests
from .utils.encontrar_primer_numero import encontrar_primer_numero

def get_attribute_value(attributes, desired_attribute):
    for att in attributes:
        if att.get("id") == desired_attribute:
            return att["value_name"]
    return None


def get_new_properties_meli():
    url = "https://api.mercadolibre.com/sites/MLU/search?category=MLU1459&q=apartament#json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print((f"Successfully fetched data from {url}"))
            results = response.json()["results"]

            filtered_results=[]
            
            for result in results:
                filtered_obj = {
                    "titulo": result["title"],
                    "tipo": get_attribute_value(result["attributes"], "PROPERTY_TYPE").lower(),
                    "cuartos": get_attribute_value(result["attributes"], "BEDROOMS"),
                    "metros_cuadrados": get_attribute_value(result["attributes"], "COVERED_AREA")[:-3],
                    "barrio": result["location"]["city"]['name'].lower(),
                    "precio": result["price"],
                    "direccion": result["location"]["address_line"],
                    "url": result["permalink"],
                }
                
                response_detail =  requests.get(f'https://api.mercadolibre.com/items/{result["id"]}')
                if response_detail.status_code == 200:
                    result_detail = response_detail.json()
                    gastos_comunes = get_attribute_value(result_detail["attributes"], "MAINTENANCE_FEE")
                    filtered_obj["gastos_comunes"] = encontrar_primer_numero(gastos_comunes) if gastos_comunes else 0

                filtered_results.append(filtered_obj)
        else:
            print((f"Failed to fetch data from {url}. Status code: {response.status_code}"))

        response_detail =  requests.get('https://api.mercadolibre.com/items/MLU-659020602')
        print(response_detail.status_code)
        if response_detail.status_code == 200:
            result_detail = response_detail.json()
            filtered_obj = {
                "titulo": result["title"],
                "tipo": get_attribute_value(result["attributes"], "PROPERTY_TYPE").lower(),
                "cuartos": get_attribute_value(result["attributes"], "BEDROOMS"),
                "metros_cuadrados": get_attribute_value(result["attributes"], "COVERED_AREA")[:-3],
                "barrio": result["location"]["city"]['name'].lower(),
                "precio": result["price"],
                "direccion": result["location"]["address_line"],
                "url": result["permalink"],
            }
            filtered_results.append(filtered_obj)

        return filtered_results
    except requests.RequestException as e:
        print((f"An error occurred: {e}"))


class Command(BaseCommand):
    """Hace una request a mercado libre para obtener los resultados de inmuebles"""

    def handle(self, *args, **kwargs):
        get_new_properties_meli()