from django.urls import path

from news.views import NewsListView, NewsDetailView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:id>/', NewsDetailView.as_view(), name='news_detail'),
]
