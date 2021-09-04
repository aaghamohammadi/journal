from django.contrib.auth.views import LoginView
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from .forms import UserRegisterForm


class RegisterView(FormView):
    template_name = 'notes/register.html'
    form_class = UserRegisterForm

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

    def get_success_url(self):
        return reverse("notes:success")


class UserLoginView(LoginView):
    template_name = 'notes/login.html'

    def get_success_url(self):
        return reverse_lazy('landing-page')


def success_view(request):
    template_name = 'notes/success.html'
    return render(request, template_name)


class LandingPageView(TemplateView):
    template_name = 'notes/landing.html'