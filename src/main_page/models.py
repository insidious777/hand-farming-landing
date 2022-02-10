from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _, pgettext_lazy

from main_page.constants import Texts, Images, Links
from main_page.utils import extract_youtube_video_code
from main_page.validators import phone_number_validator, terms_accepted_validator


class Text(models.Model):
    text = models.CharField(max_length=255, verbose_name=_('Text'))

    class TextTypes(models.TextChoices):
        NAVBAR_ABOUT_US = (Texts.NAVBAR_ABOUT_US, _('Navbar about us'))
        NAVBAR_OUR_IDEA = (Texts.NAVBAR_OUR_IDEA, _('Navbar our idea'))
        NAVBAR_REVIEWS = (Texts.NAVBAR_REVIEWS, _('Navbar reviews'))
        NAVBAR_NEWS = (Texts.NAVBAR_NEWS, _('Navbar news'))
        NAVBAR_CONTACTS = (Texts.NAVBAR_CONTACTS, _('Navbar contacts'))

        LANG_SELECTOR_UK_TEXT = (Texts.LANG_SELECTOR_UK_TEXT, _('Language selector ukrainian text'))
        LANG_SELECTOR_RU_TEXT = (Texts.LANG_SELECTOR_RU_TEXT, _('Language selector russian text'))
        LANG_SELECTOR_EN_TEXT = (Texts.LANG_SELECTOR_EN_TEXT, _('Language selector english text'))

        PAGE_MAIN_TITLE = (Texts.PAGE_MAIN_TITLE, _('Page main title'))
        PAGE_MAIN_SUBTITLE = (Texts.PAGE_MAIN_SUBTITLE, _('Page main subtitle'))
        GO_TO_STORE_BUTTON_TEXT = (Texts.GO_TO_STORE_BUTTON_TEXT, _('Go to store button text'))
        YOUTUBE_TITLE = (Texts.YOUTUBE_TITLE, _('Youtube title'))
        YOUTUBE_CHANNEL_NAME = (Texts.YOUTUBE_CHANNEL_NAME, _('Youtube channel name'))

        QUESTIONS_SECTION_TITLE = (Texts.QUESTIONS_SECTION_TITLE, _('Questions section title'))

        STORIES_SECTION_TITLE = (Texts.STORIES_SECTION_TITLE, _('Stories section title'))
        STORY_READ_MORE_BUTTON_TEXT = (Texts.STORY_READ_MORE_BUTTON_TEXT, _('Story read more button text'))

        NEWS_SECTION_TITLE = (Texts.NEWS_SECTION_TITLE, _('News section title'))
        READ_MORE_NEWS_BUTTON_TEXT = (Texts.READ_MORE_NEWS_BUTTON_TEXT, _('Read more news button text'))

        CONTACTS_SECTION_TITLE = (Texts.CONTACTS_SECTION_TITLE, _('Contacts section title'))
        CONTACTS_ADDRESS_TEXT = (Texts.CONTACTS_ADDRESS_TEXT, _('Contacts address text'))
        CONTACTS_ADDRESS = (Texts.CONTACTS_ADDRESS, _('Contacts address'))
        CONTACTS_PHONE_NUMBER_TEXT = (Texts.CONTACTS_PHONE_NUMBER_TEXT, _('Contacts phone number text'))
        CONTACTS_PHONE_NUMBER = (Texts.CONTACTS_PHONE_NUMBER, _('Contacts phone number'))
        CONTACTS_EMAIL_TEXT = (Texts.CONTACTS_EMAIL_TEXT, _('Contacts email text'))
        CONTACTS_EMAIL = (Texts.CONTACTS_EMAIL, _('Contacts email'))

        FEEDBACK_SECTION_TITLE = (Texts.FEEDBACK_SECTION_TITLE, _('Feedback section title'))
        FEEDBACK_SECTION_SUBTITLE = (Texts.FEEDBACK_SECTION_SUBTITLE, _('Feedback section subtitle'))

        FEEDBACK_FORM_NAME_PLACEHOLDER = (Texts.FEEDBACK_FORM_NAME_PLACEHOLDER, _('Feedback form name placeholder'))
        FEEDBACK_FORM_PHONE_NUMBER_PLACEHOLDER = (Texts.FEEDBACK_FORM_PHONE_NUMBER_PLACEHOLDER, _('Feedback form phone number placeholder'))
        FEEDBACK_FORM_EMAIL_PLACEHOLDER = (Texts.FEEDBACK_FORM_EMAIL_PLACEHOLDER, _('Feedback form email placeholder'))
        FEEDBACK_FORM_MESSAGE_PLACEHOLDER = (Texts.FEEDBACK_FORM_MESSAGE_PLACEHOLDER, _('Feedback form message placeholder'))
        FEEDBACK_FORM_TERMS_TEXT = (Texts.FEEDBACK_FORM_TERMS_TEXT, _('Feedback form terms text'))
        FEEDBACK_FORM_SUBMIT_BUTTON_TEXT = (Texts.FEEDBACK_FORM_SUBMIT_BUTTON_TEXT, _('Feedback form submit button text'))
        FEEDBACK_FORM_SUCCESS_MESSAGE = (Texts.FEEDBACK_FORM_SUCCESS_MESSAGE, _('Feedback form success message'))

        # From news
        SHARE_NEWS = (Texts.SHARE_NEWS, _('Share news'))
        READ_OTHER_NEWS = (Texts.READ_OTHER_NEWS, _('Read other news'))
        COPY_NEWS_LINK = (Texts.COPY_NEWS_LINK, _('Copy news link'))

    type = models.CharField(max_length=255, choices=TextTypes.choices, unique=True, verbose_name=_('Type'))

    class Meta:
        verbose_name = _('Text')
        verbose_name_plural = _('Texts')

    def __str__(self):
        return _('Text: %(type_display)s') % {'type_display': self.get_type_display()}

    def get_text_marked_as_safe(self):
        return mark_safe(self.text)


class Image(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'), blank=True)
    alt = models.CharField(max_length=255, verbose_name=_('Alternative text'), help_text=_('If image cannot be loaded, then this text will be shown'))
    file = models.ImageField(upload_to='images', verbose_name=_('File'))

    class ImageTypes(models.TextChoices):
        NAVBAR_BRAND = (Images.NAVBAR_BRAND, _('Navbar brand image'))
        BOTTOM_NAVBAR_BRAND = (Images.BOTTOM_NAVBAR_BRAND, _('Bottom navbar brand image'))
        HEADER_BACKGROUND = (Images.HEADER_BACKGROUND, _('Header background image'))
        ABOUT_HAND_FARMING = (Images.ABOUT_HAND_FARMING, _('About hand farming image'))
        GO_TO_OUR_YOUTUBE_CHANNEL_ICON = (Images.GO_TO_OUR_YOUTUBE_CHANNEL_ICON, _('Go to our youtube channel icon'))
        GET_IT_ON_GOOGLE_PLAY = (Images.GET_IT_ON_GOOGLE_PLAY, _('Get it on Google Play image'))
        DOWNLOAD_ON_THE_APP_STORE = (Images.DOWNLOAD_ON_THE_APP_STORE, _('Download on the App Store image'))
        FACEBOOK_SOCIAL_MEDIA_ICON = (Images.FACEBOOK_SOCIAL_MEDIA_ICON, _('Facebook social media icon'))
        INSTAGRAM_SOCIAL_MEDIA_ICON = (Images.INSTAGRAM_SOCIAL_MEDIA_ICON, _('Instagram social media icon'))
        YOUTUBE_SOCIAL_MEDIA_ICON = (Images.YOUTUBE_SOCIAL_MEDIA_ICON, _('Youtube social media icon'))

        # From news
        SHARE_NEWS_ON_FACEBOOK = (Images.SHARE_NEWS_ON_FACEBOOK, _('Share news on facebook'))

    type = models.CharField(max_length=255, choices=ImageTypes.choices, unique=True, verbose_name=_('Type'))

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    @property
    def url(self):
        return self.file.url

    def __str__(self):
        return _('Image: %(type_display)s') % {'type_display': self.get_type_display()}


class AboutUs(models.Model):
    image = models.ImageField(upload_to='images', verbose_name=_('Image'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    subtitle = models.CharField(max_length=255, verbose_name=_('Subtitle'))
    text = RichTextField(verbose_name=_('Text'))

    class Meta:
        verbose_name = _('About us')
        verbose_name_plural = _('About us')

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name=_('Text'))
    youtube_video_url = models.URLField(verbose_name=_('Youtube video url'))
    youtube_video_code = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Youtube video code'), help_text=_('Example: URL - https://www.youtube.com/watch?v=19bbXiGbfdk then video code is - 19bbXiGbfdk<br>Leave blank and video code will be detected automatically<br>If after saving this field still empty - fill it manually'))
    show = models.BooleanField(default=True, verbose_name=pgettext_lazy('show something on site or not', 'Show'))

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return _('Question: %(type_display)s') % {'type_display': self.text}

    def save(self, *args, **kwargs):
        if self.youtube_video_url and not self.youtube_video_code:
            self.youtube_video_code = extract_youtube_video_code(self.youtube_video_url)

        super().save(*args, **kwargs)

    @property
    def youtube_embed_url(self):
        return f'https://www.youtube.com/embed/{self.youtube_video_code}'


class Story(models.Model):
    image = models.ImageField(upload_to='stories', verbose_name=_('Image'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    subtitle = models.CharField(max_length=255, verbose_name=_('Subtitle'))
    url = models.URLField(verbose_name=_('URL'))
    show = models.BooleanField(default=True, verbose_name=pgettext_lazy('show something on site or not', 'Show'))

    class Meta:
        verbose_name = _('Story')
        verbose_name_plural = _('Stories')

    def __str__(self):
        return _('Story: %(type_display)s') % {'type_display': self.title}


class Link(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    url = models.URLField(verbose_name=_('URL'))

    class LinkTypes(models.TextChoices):
        FACEBOOK = (Links.FACEBOOK, _('Facebook'))
        INSTAGRAM = (Links.INSTAGRAM, _('Instagram'))
        YOUTUBE = (Links.YOUTUBE, _('Youtube'))
        HAND_FARMING_APP_ON_GOOGLE_PLAY = (Links.HAND_FARMING_APP_ON_GOOGLE_PLAY, _('Download Hand Farming app on Google Play'))
        HAND_FARMING_APP_ON_APP_STORE = (Links.HAND_FARMING_APP_ON_APP_STORE, _('Download Hand Farming app on App Store'))
        HAND_FARMING_SHOP = (Links.HAND_FARMING_SHOP, _('Hand Farming shop'))
        QUESTIONS_SECTION_DEFAULT_VIDEO_URL = (Links.QUESTIONS_SECTION_DEFAULT_VIDEO_URL, _('Questions section default video URL'))

    type = models.CharField(max_length=255, choices=LinkTypes.choices, unique=True, verbose_name=_('Type'))

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')

    def __str__(self):
        return _('Link: %(type_display)s') % {'type_display': self.get_type_display()}


class Map(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=_('Latitude'))
    lng = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=_('Longitude'))
    google_maps_api_key = models.CharField(max_length=255, verbose_name=_('Google Maps API Key'))

    class Meta:
        verbose_name = _('Map')
        verbose_name_plural = _('Maps')

    def __str__(self):
        return _('Map: %(coordinates)s') % {'coordinates': f'{self.lat},{self.lng}'}

    def save(self, *args, **kwargs):

        if self.google_maps_api_key:
            self.google_maps_api_key = self.google_maps_api_key.strip(' ')

        super().save(*args, **kwargs)


class Feedback(models.Model):
    username = models.CharField(max_length=255, verbose_name=_('Username'))
    phone_number = models.CharField(max_length=255, verbose_name=_('Phone number'), help_text=_('Format: +380XXXXXXXXX'), validators=[phone_number_validator])
    email = models.EmailField(verbose_name=_('Email'))
    message = models.TextField(verbose_name=_('Message'))
    terms_accepted = models.BooleanField(verbose_name=pgettext_lazy('whether terms accepted or not', 'Terms accepted'), validators=[terms_accepted_validator])
    received_at = models.DateTimeField(auto_now_add=True, verbose_name=pgettext_lazy('time, when something is received', 'Received at'))

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def __str__(self):
        return _('Message from %(sender)s') % {'sender': f'{self.username}, {self.phone_number}, {self.phone_number}'}
