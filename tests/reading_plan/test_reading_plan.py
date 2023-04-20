from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501

import pytest


def mock_news():
    return [
        {
            "url": "url",
            "title": "Some cool title",
            "writer": "writer",
            "summary": "summary",
            "reading_time": 2,
            "timestamp": "timestamp",
            "category": "category",
        },
        {
            "url": "url",
            "title": "Some cool title2",
            "writer": "writer",
            "summary": "summary",
            "reading_time": 5,
            "timestamp": "timestamp",
            "category": "category",
        },
        {
            "url": "url",
            "title": "Some cool title3",
            "writer": "writer",
            "summary": "summary",
            "reading_time": 3,
            "timestamp": "timestamp",
            "category": "category",
        },
    ]


result = {
    "readable": [
        {
            "unfilled_time": 0,
            "chosen_news": [("Some cool title", 2)],
        }
    ],
    "unreadable": [
        ("Some cool title2", 5),
        ("Some cool title3", 3),
    ],
}


def test_reading_plan_group_news():
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-1)

    ReadingPlanService._db_news_proxy = mock_news
    reading_plan = ReadingPlanService.group_news_for_available_time(2)
    assert reading_plan == result
