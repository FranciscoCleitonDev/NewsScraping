import requests
from bs4 import BeautifulSoup

def get_latest_news():
    url = "https://ge.globo.com/"
    tag = "a"
    classe = "feed-post-link"

    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao acessar a página:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    elementos = soup.find_all(tag, class_=classe)

    noticias = []
    for elemento in elementos[1:]:  # Ignora o primeiro elemento
        p_tag = elemento.find('p')
        if p_tag:
            noticias.append(p_tag.get_text(strip=True))

    return noticias
