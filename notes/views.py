from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import UserRegisterForm


class UserRegisterView(FormView):
    template_name = "notes/register.html"
    form_class = UserRegisterForm

    def form_valid(self, form):
        form.save()
        return super(UserRegisterView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("notes:success")


def success_view(request):
    template_name = "notes/success.html"
    return render(request, template_name)


class LandingPageView(TemplateView):
    template_name = "notes/landing.html"
