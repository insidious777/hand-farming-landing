from django import forms
from django.utils.translation import gettext_lazy as _

from common.fields import SVGAndImageFormField
from main_page.models import Image, Feedback
from main_page.validators import phone_number_validator


class ImageModelForm(forms.ModelForm):

    class Meta:
        model = Image
        exclude = []
        field_classes = {
            'file': SVGAndImageFormField,
        }


class FeedBackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('username', 'phone_number', 'email', 'terms_accepted', 'message')
