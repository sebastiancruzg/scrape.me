def get_content(item, base_url:str)->tuple:
    title_block = item.h2.a
    name = title_block.text
    url = base_url + title_block.get('href')

    try:
        reviews_block = item.find('div', {'data-cy': 'reviews-block'})
        rating = reviews_block.i.text
        reviews_amount = reviews_block.find('span', {'data-component-type': 's-client-side-analytics'}).text
    except AttributeError:
        rating = ''
        reviews_amount = ''

    try:
        price = item.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).text
    except AttributeError:
        return

    return (name, price, rating, reviews_amount, url)
