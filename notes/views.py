from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import UserRegisterForm


class RegisterView(FormView):
    template_name = 'notes/register.html'
    form_class = UserRegisterForm

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)
