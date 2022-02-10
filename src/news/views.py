from django.conf import settings
from django.db.models import F
from django.views.generic import ListView, DetailView

from common.context import get_common_context
from news.handlers import get_news, get_recommended_news
from news.models import News


class NewsListView(ListView):
    template_name = 'news_list.html'
    paginate_by = settings.NEWS_LIST_PAGINATE_BY
    http_method_names = ['get']
    context_object_name = 'news_list'

    def get_queryset(self):
        return get_news()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(get_common_context())
        return context

    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())

        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1

        try:
            page_number = int(page)
        except:
            page_number = 1

        try:
            page = paginator.page(page_number)
        except:
            page = paginator.page(paginator.num_pages)

        return paginator, page, page.object_list, page.has_other_pages()


class NewsDetailView(DetailView):
    pk_url_kwarg = 'id'
    model = News
    template_name = 'news_detail.html'

    VISITED_SESSION_KEY_PREFIX = 'news_visited_'

    def get_queryset(self):
        return get_news()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = context.get('news')

        context.update({
            **get_common_context(),
            'recommended_news': get_recommended_news(news)
        })

        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        self.check_visited(obj)
        return obj

    def check_visited(self, obj):
        session = self.request.session
        visited_key = self.get_visited_session_key(obj)

        if not session.get(visited_key):
            obj.views_count = F('views_count') + 1
            obj.save()
            session[visited_key] = True

    def get_visited_session_key(self, obj):
        return f'{self.VISITED_SESSION_KEY_PREFIX}{obj.id}'
