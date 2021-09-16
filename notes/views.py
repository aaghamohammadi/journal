from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegisterForm
from .models import Item


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


class LandingPageView(LoginRequiredMixin, ListView):
    template_name = "notes/landing.html"
    redirect_field_name = ""

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(user=user)
