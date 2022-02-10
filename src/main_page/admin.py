from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import pgettext_lazy, gettext_lazy as _

from modeltranslation.admin import TabbedTranslationAdmin

from main_page.forms import ImageModelForm
from main_page.models import Text, Image, Question, Story, Link, Map, AboutUs, Feedback


@admin.register(Text)
class TextModelAdmin(TabbedTranslationAdmin):
    search_fields = ['text']
    list_filter = ['type']
    list_display = ['text', 'type']


@admin.register(Image)
class ImageModelAdmin(TabbedTranslationAdmin):
    form = ImageModelForm
    search_fields = ['title', 'alt', 'file__name', 'type']
    list_filter = ['type']
    list_display = ['preview', 'type']

    @admin.display(description=pgettext_lazy('Image preview', 'Preview'), ordering='file')
    def preview(self, obj):
        return mark_safe(f'<img style="max-height: 50px; object-fit: cover;" src="{obj.url}" alt="{obj.alt}">')


@admin.register(AboutUs)
class AboutUsModelAdmin(TabbedTranslationAdmin):

    def has_add_permission(self, request):
        return AboutUs.objects.count() == 0


@admin.register(Question)
class QuestionModelAdmin(TabbedTranslationAdmin):
    list_display = ['text', 'link', 'show']
    list_filter = ['show']
    search_fields = ['text', 'youtube_video_url', 'youtube_video_code']

    def link(self, obj):
        return mark_safe(f'<a href="{obj.youtube_embed_url}" target="_blank">{obj.youtube_embed_url}</a>')


@admin.register(Story)
class StoryModelAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'link', 'show']
    list_filter = ['show']
    search_fields = ['title', 'subtitle', 'url', 'image__name']

    @admin.display(description=_('Link'), ordering='url')
    def link(self, obj):
        return mark_safe(f'<a href="{obj.url}" target="_blank">{obj.url}</a>')


@admin.register(Link)
class LinkModelAdmin(TabbedTranslationAdmin):
    list_display = ['type', 'link']
    list_filter = ['type']

    @admin.display(description=_('Link'), ordering='url')
    def link(self, obj):
        return mark_safe(f'<a href="{obj.url}" target="_blank">{obj.url}</a>')


@admin.register(Map)
class MapModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return Map.objects.count() == 0


@admin.register(Feedback)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'email', 'received_at']
    list_filter = ['received_at']
    search_fields = ['username', 'phone_number', 'email', 'message', 'received_at']
    ordering = ['-received_at']

    readonly_fields = ['username', 'phone_number', 'email', 'message', 'terms_accepted']

    def has_add_permission(self, request):
        return False
