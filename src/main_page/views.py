from django.http import JsonResponse, HttpResponseForbidden
from django.views import View
from django.views.generic import TemplateView

from common.context import get_common_context
from main_page.forms import FeedBackForm
from main_page.handlers import get_about_us, get_questions, get_stories, get_map, notify_about_new_feedback
from news.handlers import get_last_three_news


class MainPageView(TemplateView):
    template_name = 'main_page.html'
    http_method_names = ['get']
    FORM_SUBMITTED_SESSION_KEY = 'form_submitted'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            **get_common_context(),
            'about_us': get_about_us(),
            'questions': get_questions(),
            'stories': get_stories(),
            'news': get_last_three_news(),
            'map': get_map(),
            'form_submitted': self.request.session.get(self.FORM_SUBMITTED_SESSION_KEY, False)
        })

        return context


class ReceiveFeedback(View):
    http_method_names = ['post']
    FORM_SUBMITTED_SESSION_KEY = 'form_submitted'

    def post(self, request):

        if self.request.session.get(self.FORM_SUBMITTED_SESSION_KEY, False):
            return HttpResponseForbidden()

        form = FeedBackForm(request.POST)
        if form.is_valid():
            feedback = form.save()

            request.session[self.FORM_SUBMITTED_SESSION_KEY] = True
            request.session.set_expiry(0)   # session expires when user's browser is closed

            notify_about_new_feedback(feedback)
            return JsonResponse({'status': 'success'})

        else:
            errors = form.errors
            return JsonResponse({'status': 'error', 'errors': errors})
