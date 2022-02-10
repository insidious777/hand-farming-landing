from django.urls import path

from main_page.views import MainPageView, ReceiveFeedback

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('feedback/', ReceiveFeedback.as_view(), name='receive_feedback'),
]
