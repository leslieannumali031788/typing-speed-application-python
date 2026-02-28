from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


def getWikiPageWords(input):
    url_prefix = 'https://en.wikipedia.org/wiki/'
    url = url_prefix + input

    req = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    html = urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')

    all_ps = soup.find_all(lambda tag: tag.name == 'p' and not tag.attrs, limit=5)
    all_ps = [s.get_text() for s in all_ps]
    all_ps = ' '.join(all_ps)

    after_sub = re.sub(r"(\[\d+])|(\n)", "", all_ps)

    return after_sub