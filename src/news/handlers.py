from news.models import News


def get_last_three_news():
    return get_news()[:3]


def get_recommended_news(news):
    return get_news().exclude(id=news.id)[:3]


def get_news():
    return News.objects.filter(show=True).order_by('-display_date')
