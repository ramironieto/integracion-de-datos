from django.core.management.base import BaseCommand
import requests

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
                    "tipo": get_attribute_value(result["attributes"], "PROPERTY_TYPE"),
                    "cuartos": get_attribute_value(result["attributes"], "BEDROOMS"),
                    "metros_cuadrados": get_attribute_value(result["attributes"], "COVERED_AREA")[:-3],
                    "barrio": result["address"]["city_name"],
                    "precio": result["price"],
                    "gastos_comunes": get_attribute_value(result["attributes"], "MAINTENANCE_FEE"),
                    "direccion": result["location"]["address_line"],
                }
                filtered_results.append(filtered_obj)
            return filtered_results
        else:
            print((f"Failed to fetch data from {url}. Status code: {response.status_code}"))
    except requests.RequestException as e:
        print((f"An error occurred: {e}"))


class Command(BaseCommand):
    """Hace una request a mercado libre para obtener los resultados de inmuebles"""

    def handle(self, *args, **kwargs):
        get_new_properties_meli()