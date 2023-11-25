from selenium.webdriver.common.by import By
from selenium import webdriver

def scrape_property_data(url):
    browser = webdriver.Chrome(executable_path='/Users/joaco/Downloads/chromedriver-mac-arm64/chromedriver')
    browser.get(url)

    inmueble = {
        'titulo': browser.find_element(By.CLASS_NAME, 'titulo').text.strip(),
        'tipo': find_label_by_icon(browser, 'fa-building'),
        'cuartos': find_label_by_icon(browser, 'fa-bed'),
        'metros_cuadrados': find_in_caracteristicas(browser, 'Sup. construida:'),
        'barrio': find_label_by_icon(browser, 'fa-map-marked'),
        'precio': browser.find_element(By.CLASS_NAME, 'precio').text.strip(),
        'gastos_comunes': find_in_caracteristicas(browser, 'Gastos Comunes'),
        'direccion': browser.find_element(By.CLASS_NAME, 'direccion').text.strip(),
        'url': url,
    }
    return inmueble

def find_label_by_icon(browser, icon):
    try:
        icon_selector = f'//i[contains(@class, \'{icon}\')]'
        icono = browser.find_element(By.XPATH, icon_selector)
        return icono.find_element(By.XPATH, './ancestor::div[@class=\'wrapperDatos\']/p').text.strip()
    except:
        return None
    
def find_in_caracteristicas(browser, caracteristica):
    try:
        ul_caracteristicas = browser.find_element(By.ID, 'ul_caracteristicas')
        caracteristica_selector = f'//li[contains(text(), \'{caracteristica}\')]'
        return ul_caracteristicas.find_element(By.XPATH, caracteristica_selector).text.strip()
    except:
        return None