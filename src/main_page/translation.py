from modeltranslation.translator import register, TranslationOptions
from .models import Text, Image, Question, Story, Link, AboutUs


@register(Text)
class TextTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Image)
class ImageTranslationOptions(TranslationOptions):
    fields = ('title', 'alt')


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'text')


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Story)
class StoryTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


@register(Link)
class LinkTranslationOptions(TranslationOptions):
    fields = ('title',)
