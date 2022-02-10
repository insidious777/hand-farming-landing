from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from news.models import News


@admin.register(News)
class NewsModelAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'display_date', 'views_count', 'show']
    list_filter = ['show', 'display_date']
    search_fields = ['title', 'short_description', 'text', 'display_date']
