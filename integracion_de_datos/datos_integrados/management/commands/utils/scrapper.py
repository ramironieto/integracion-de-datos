import requests
from bs4 import BeautifulSoup

def scrape_property_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        inmueble = {
            "titulo": soup.find('span', {'class': 'titulo'}).text.strip(),
            "tipo": soup.find('span', {'class': 'tipo'}).text.strip(),
            "cuartos": soup.find('span', {'class': 'cuartos'}).text.strip(),
            "metros_cuadrados": soup.find('span', {'class': 'metros cuadrados'}).text.strip(),
            "barrio": soup.find('span', {'class': 'barrio'}).text.strip(),
            "precio": soup.find('span', {'class': 'precio'}).text.strip(),
            "gastos_comunes": soup.find('span', {'class': 'gastos comunes'}).text.strip(),
            "direccion": soup.find('span', {'class': 'direccion'}).text.strip(),
            "url": url,
        }

        print(inmueble)
        
        return inmueble
    else:
        print("Failed to fetch the page")
        return None

