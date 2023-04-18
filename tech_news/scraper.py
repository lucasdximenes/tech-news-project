import requests
from time import sleep

BASE_URL = "https://blog.betrybe.com/"


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            BASE_URL, headers={"User-Agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.Timeout:
        return None
    finally:
        sleep(1)


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
