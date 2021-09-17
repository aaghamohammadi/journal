from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
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
    context_object_name = "items"

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(user=user)


class ItemPageView(LoginRequiredMixin, DetailView):
    template_name = "notes/item.html"
    redirect_field_name = ""
    context_object_name = "item"

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ["text", "title"]
    template_name = "notes/create.html"
    redirect_field_name = ""
    success_url = reverse_lazy("notes:landing-page")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)
