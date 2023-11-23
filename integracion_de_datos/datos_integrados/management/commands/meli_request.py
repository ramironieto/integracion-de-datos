from django.core.management.base import BaseCommand
import requests

def get_attribute_value(attributes, desired_attribute):
    for att in attributes:
        if att.get("id") == desired_attribute:
            return att["value_name"]
    return None

class Command(BaseCommand):
    """Hace una request a mercado libre para obtener los resultados de inmuebles"""

    def handle(self, *args, **kwargs):
        url = "https://api.mercadolibre.com/sites/MLU/search?category=MLU1459&q=apartament#json"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.stdout.write(self.style.SUCCESS(f"Successfully fetched data from {url}"))
                results = response.json()["results"]
                desired_fields = ['price',"description","title"]

                filtered_results=[]
                
                for result in results:
                    filtered_obj = {
                        "precio": result["price"],
                        "barrio": result["address"]["city_name"],
                        "gastos_comunes": get_attribute_value(result["attributes"], "MAINTENANCE_FEE"),
                        "metros_cuadrados": get_attribute_value(result["attributes"], "COVERED_AREA"),
                        "direccion": result["location"]["address_line"],
                        "tipo": get_attribute_value(result["attributes"], "PROPERTY_TYPE"),
                        "cuartos": get_attribute_value(result["attributes"], "BEDROOMS"),
                        "titulo": result["title"],
                    }
                    filtered_results.append(filtered_obj)

                    print(f"{filtered_obj} \n")
            else:
                self.stdout.write(self.style.ERROR(f"Failed to fetch data from {url}. Status code: {response.status_code}"))
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
