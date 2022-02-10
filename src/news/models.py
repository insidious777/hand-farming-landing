from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _, pgettext_lazy


class News(models.Model):
    image = models.ImageField(upload_to='news', verbose_name=_('Image'))
    display_date = models.DateField(verbose_name=pgettext_lazy('which date will be shown', 'Display date'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    short_description = models.CharField(max_length=255, verbose_name=_('Short description'))
    text = RichTextUploadingField(verbose_name=_('Text'))

    show = models.BooleanField(default=False, verbose_name=pgettext_lazy('show something on site or not', 'Show'))
    views_count = models.IntegerField(default=0, verbose_name=pgettext_lazy('how many times something is viewed', 'Views count'))

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return _('News: %(type_display)s') % {'type_display': self.title}
