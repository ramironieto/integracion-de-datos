from selenium.webdriver.common.by import By
from selenium import webdriver

url = "http://legendas.tv/busca/walking%20dead%20s03e02"


def scrape_property_data(url):
    browser = webdriver.Chrome(executable_path='/Users/rnieto/Downloads/chromedriver-mac-arm64/chromedriver')
    browser.get(url)

    inmueble = {
        "titulo": browser.find_element(By.CLASS_NAME, 'titulo').text.strip(),
        "tipo": browser.find_element(By.CLASS_NAME, 'tipo').text.strip(),
        "cuartos": browser.find_element(By.CLASS_NAME, 'cuartos').text.strip(),
        "metros_cuadrados": browser.find_element(By.CLASS_NAME, 'metros_cuadrados').text.strip(),
        "barrio": browser.find_element(By.CLASS_NAME, 'barrio').text.strip(),
        "precio": browser.find_element(By.CLASS_NAME, 'precio').text.strip(),
        "gastos_comunes": browser.find_element(By.CLASS_NAME, 'gastos_comunes').text.strip(),
        "direccion": browser.find_element(By.CLASS_NAME, 'direccion').text.strip(),
        "url": url,
    }
    return inmueble

