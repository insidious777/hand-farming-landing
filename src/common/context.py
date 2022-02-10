from django.conf import settings

from main_page.handlers import get_texts_for_render_context, get_images_for_render_context, get_links_for_render_context


def get_common_context():
    return {
        'texts': get_texts_for_render_context(),
        'images': get_images_for_render_context(),
        'links': get_links_for_render_context(),
        'settings': settings
    }
