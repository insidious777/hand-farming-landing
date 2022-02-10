from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.utils import translation

from main_page.models import Text, Image, Link, AboutUs, Question, Story, Map


def get_texts():
    return Text.objects.all()


def get_text_types():
    return Text.TextTypes.names


def get_texts_for_render_context():
    texts = get_texts()
    text_map = {}

    for text_type in get_text_types():
        text_map.update({text_type: texts.filter(type=text_type).first()})

    return text_map


def get_images():
    return Image.objects.all()


def get_image_types():
    return Image.ImageTypes.names


def get_images_for_render_context():
    images = get_images()
    image_map = {}

    for image_type in get_image_types():
        image_map.update({image_type: images.filter(type=image_type).first()})

    return image_map


def get_links():
    return Link.objects.all()


def get_link_types():
    return Link.LinkTypes.names


def get_links_for_render_context():
    links = get_links()
    link_map = {}

    for link_type in get_link_types():
        link_map.update({link_type: links.filter(type=link_type).first()})

    return link_map


def get_about_us():
    return AboutUs.objects.first()


def get_questions():
    return Question.objects.filter(show=True)


def get_stories():
    return Story.objects.filter(show=True)[:settings.MAIN_PAGE_STORIES_COUNT]


def get_map():
    return Map.objects.first()


def notify_about_new_feedback(feedback):

    for language, email_to in settings.NOTIFY_NEW_FEEDBACK_EMAILS:

        with translation.override(language):
            subject = loader.render_to_string('feedback_notification_mail_subject.txt', {'username': feedback.username})
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())

            body_context = {
                'username': feedback.username,
                'phone_number': feedback.phone_number,
                'email': feedback.email,
                'message': feedback.message,
            }
            message = loader.render_to_string('feedback_notification_mail_template.html', body_context)
            html_message = loader.render_to_string('feedback_notification_mail_html_template.html', body_context)

            send_mail(
                subject,
                message,
                settings.EMAIL_FROM,
                [email_to],
                html_message=html_message,
                fail_silently=True,
            )
