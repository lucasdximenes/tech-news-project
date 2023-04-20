from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    # Seu código
    all_news_categories = [news["category"] for news in find_news()]
    categories = set(all_news_categories)
    categories_count = {
        category: all_news_categories.count(category)
        for category in categories
    }
    categories_count = sorted(
        categories_count.items(), key=lambda x: (-x[1], x[0])
    )
    return [category[0] for category in categories_count[:5]]
