# Generated by Django 3.2.2 on 2021-05-13 19:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='subtitle_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_uk',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='image',
            name='type',
            field=models.CharField(choices=[('NAVBAR_BRAND', 'Navbar brand image'), ('BOTTOM_NAVBAR_BRAND', 'Bottom navbar brand image'), ('HEADER_BACKGROUND', 'Header background image'), ('ABOUT_HAND_FARMING', 'About hand farming image'), ('GO_TO_OUR_YOUTUBE_CHANNEL_ICON', 'Go to our youtube channel icon'), ('GET_IT_ON_GOOGLE_PLAY', 'Get it on Google Play image'), ('DOWNLOAD_ON_THE_APP_STORE', 'Download on the App Store image'), ('FACEBOOK_SOCIAL_MEDIA_ICON', 'Facebook social media icon'), ('INSTAGRAM_SOCIAL_MEDIA_ICON', 'Instagram social media icon'), ('YOUTUBE_SOCIAL_MEDIA_ICON', 'Youtube social icon')], max_length=255, unique=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='link',
            name='type',
            field=models.CharField(choices=[('FACEBOOK', 'Facebook'), ('INSTAGRAM', 'Instagram'), ('YOUTUBE', 'Youtube'), ('HAND_FARMING_APP_ON_GOOGLE_PLAY', 'Download Hand Farming app on Google Play'), ('HAND_FARMING_APP_ON_APP_STORE', 'Download Hand Farming app on App Store'), ('HAND_FARMING_SHOP', 'Hand Farming shop')], max_length=255, unique=True, verbose_name='Type'),
        ),
    ]
