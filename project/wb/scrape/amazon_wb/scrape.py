from ..set_up_driver import setup_chrome_driver
from .get_url import get_url
from .get_content import get_content
from .collect_products import collect_products

def scrape(base_url:str, search_term:str, save_model:callable)->None:

    driver = setup_chrome_driver()

    records = []
    for i in range(1, 7):
        url = get_url(base_url, search_term, i)
        driver.get(url)
        products = collect_products(driver)

        for product in products:
            content = get_content(product, base_url)
            if content is None:
                continue
            records.append(content)

    driver.quit()
    return save_model(records)
