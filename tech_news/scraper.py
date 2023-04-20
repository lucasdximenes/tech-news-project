import requests
from parsel import Selector
from time import sleep


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"User-Agent": "Fake user-agent"}, timeout=3
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
    html_body = Selector(text=html_content)
    news_url = html_body.css("link[rel=canonical]::attr(href)").get()
    news_title = html_body.css("h1.entry-title::text").get().strip()
    news_timestamp = html_body.css(".meta-date::text").re_first(
        r"\d{2}/\d{2}/\d{4}"
    )
    news_writer = html_body.css(".author a::text").get()
    news_reading_time = int(
        html_body.css(".meta-reading-time::text").re_first(r"\d+")
    )
    news_summary = "".join(
        html_body.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    news_category = html_body.css(".category-style span.label::text").get()

    return {
        "url": news_url,
        "title": news_title,
        "timestamp": news_timestamp,
        "writer": news_writer,
        "reading_time": news_reading_time,
        "summary": news_summary,
        "category": news_category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
