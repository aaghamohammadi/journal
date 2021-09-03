from django.shortcuts import render, reverse
from django.views.generic.edit import FormView

from .forms import UserRegisterForm


class RegisterView(FormView):
    template_name = 'notes/register.html'
    form_class = UserRegisterForm

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

    def get_success_url(self):
        return reverse("notes:success")


def success_view(request):
    template_name = 'notes/success.html'
    return render(request, template_name)
