from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["items"] = context["items"].filter(title__icontains=search_input)
            context["search_input"] = search_input
        return context


class ItemPageView(LoginRequiredMixin, DetailView):
    template_name = "notes/item.html"
    redirect_field_name = ""
    context_object_name = "item"

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ["text", "title"]
    redirect_field_name = ""
    success_url = reverse_lazy("notes:landing-page")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ["text", "title"]
    redirect_field_name = ""
    success_url = reverse_lazy("notes:landing-page")


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    context_object_name = "item"
    redirect_field_name = ""
    success_url = reverse_lazy("notes:landing-page")
