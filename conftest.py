import pytest
import re
import requests

@pytest.fixture(scope="session", autouse=True)
def cleanup():
    with open("wrong_status.txt", "w") as f:
        f.write("")
    with open("noncanonical_url.txt", "w") as f:
        f.write("")
        


@pytest.fixture
def regexp():
    return re.compile(r'rel=\"canonical\"\shref=\"([\s\S]+?)\"')

def urls():
    regexp = re.compile(r"<loc>([\s\S]+?)<\/loc>")
    sitemap_url = "https://mospolytech.ru/sitemap-files.xml" #Ссылка на сайтмап
    sitemap_response = requests.get(sitemap_url)
    if sitemap_response.status_code != 200:
        raise Exception("Sitemap unavailable")
    urls_list = regexp.findall(sitemap_response.text)
    return urls_list

urls_list = urls()