import requests
from parsel import Selector
from time import sleep

BASE_URL = "https://blog.betrybe.com/"


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            BASE_URL, headers={"User-Agent": "Fake user-agent"}, timeout=3
        )
        print(response)
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
    html_body = Selector(text=html_content)
    news_card_links = html_body.css(".cs-overlay-link::attr(href)").getall()
    return news_card_links


# Requisito 3
def scrape_next_page_link(html_content):
    html_body = Selector(text=html_content)
    next_page_link = html_body.css(".next::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
