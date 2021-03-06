# Generated by Django 3.2.2 on 2021-05-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_auto_20210514_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='type',
            field=models.CharField(choices=[('NAVBAR_BRAND', 'Navbar brand image'), ('BOTTOM_NAVBAR_BRAND', 'Bottom navbar brand image'), ('HEADER_BACKGROUND', 'Header background image'), ('ABOUT_HAND_FARMING', 'About hand farming image'), ('GO_TO_OUR_YOUTUBE_CHANNEL_ICON', 'Go to our youtube channel icon'), ('GET_IT_ON_GOOGLE_PLAY', 'Get it on Google Play image'), ('DOWNLOAD_ON_THE_APP_STORE', 'Download on the App Store image'), ('FACEBOOK_SOCIAL_MEDIA_ICON', 'Facebook social media icon'), ('INSTAGRAM_SOCIAL_MEDIA_ICON', 'Instagram social media icon'), ('YOUTUBE_SOCIAL_MEDIA_ICON', 'Youtube social media icon'), ('SHARE_NEWS_ON_FACEBOOK', 'Share news on facebook')], max_length=255, unique=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='text',
            name='type',
            field=models.CharField(choices=[('NAVBAR_ABOUT_US', 'Navbar about us'), ('NAVBAR_OUR_IDEA', 'Navbar our idea'), ('NAVBAR_REVIEWS', 'Navbar reviews'), ('NAVBAR_NEWS', 'Navbar news'), ('NAVBAR_CONTACTS', 'Navbar contacts'), ('LANG_SELECTOR_UK_TEXT', 'Language selector ukrainian text'), ('LANG_SELECTOR_RU_TEXT', 'Language selector russian text'), ('LANG_SELECTOR_EN_TEXT', 'Language selector english text'), ('PAGE_MAIN_TITLE', 'Page main title'), ('PAGE_MAIN_SUBTITLE', 'Page main subtitle'), ('GO_TO_STORE_BUTTON_TEXT', 'Go to store button text'), ('YOUTUBE_TITLE', 'Youtube title'), ('YOUTUBE_CHANNEL_NAME', 'Youtube channel name'), ('QUESTIONS_SECTION_TITLE', 'Questions section title'), ('STORIES_SECTION_TITLE', 'Stories section title'), ('STORY_READ_MORE_BUTTON_TEXT', 'Story read more button text'), ('NEWS_SECTION_TITLE', 'News section title'), ('READ_MORE_NEWS_BUTTON_TEXT', 'Read more news button text'), ('CONTACTS_SECTION_TITLE', 'Contacts section title'), ('CONTACTS_ADDRESS_TEXT', 'Contacts address text'), ('CONTACTS_ADDRESS', 'Contacts address'), ('CONTACTS_PHONE_NUMBER_TEXT', 'Contacts phone number text'), ('CONTACTS_PHONE_NUMBER', 'Contacts phone number'), ('CONTACTS_EMAIL_TEXT', 'Contacts email text'), ('CONTACTS_EMAIL', 'Contacts email'), ('FEEDBACK_SECTION_TITLE', 'Feedback section title'), ('FEEDBACK_SECTION_SUBTITLE', 'Feedback section subtitle'), ('FEEDBACK_FORM_NAME_PLACEHOLDER', 'Feedback form name placeholder'), ('FEEDBACK_FORM_PHONE_NUMBER_PLACEHOLDER', 'Feedback form phone number placeholder'), ('FEEDBACK_FORM_EMAIL_PLACEHOLDER', 'Feedback form email placeholder'), ('FEEDBACK_FORM_MESSAGE_PLACEHOLDER', 'Feedback form message placeholder'), ('FEEDBACK_FORM_TERMS_TEXT', 'Feedback form terms text'), ('FEEDBACK_FORM_SUBMIT_BUTTON_TEXT', 'Feedback form submit button text'), ('SHARE_NEWS', 'Share news')], max_length=255, unique=True, verbose_name='Type'),
        ),
    ]
