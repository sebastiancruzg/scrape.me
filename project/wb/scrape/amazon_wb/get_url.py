
def get_url(url_base:str, search_term:str, page:int)->str:
    search_term = search_term.replace(' ', '+')
    url = url_base + f"s?k={search_term}&page={page}&crid=295FXWY28VWW2&ref=nb_sb_ss_recent_2_0_recent"

    return url
