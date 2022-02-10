from modeltranslation.translator import register, TranslationOptions

from news.models import News


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'text')
