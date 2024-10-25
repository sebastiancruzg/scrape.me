from bs4 import BeautifulSoup

def collect_products(driver)->list:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})
    return results
