from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import reverse
from django.test import TestCase

from .forms import UserRegisterForm

User = get_user_model()


class LandingPageViewTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("landing-page"))
        template_name = "notes/landing.html"
        self.assertTemplateUsed(response, template_name)


class UserRegisterViewTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse("notes:register"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("notes:register"))
        template_name = "notes/register.html"
        self.assertTemplateUsed(response, template_name)

    def test_register_view_uses_custom_user_register_form(self):
        response = self.client.get(reverse("notes:register"))
        self.assertIsInstance(response.context["form"], UserRegisterForm)

    def test_successful_registration_should_redirect_user_to_success_page(self):
        template_name = "notes/success.html"
        data = {
            "username": "sarahkhosravi",
            "email": "sarah@gmail.com",
            "password1": "Rted#2s@mks",
            "password2": "Rted#2s@mks",
        }

        response = self.client.post(reverse("notes:register"), data, follow=True)

        self.assertRedirects(response, reverse("notes:success"))
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)

        user = User.objects.get(username=data["username"])

        self.assertEqual(user.email, data["email"])


class SuccessViewTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse("notes:success"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("notes:success"))
        template_name = "notes/success.html"
        self.assertTemplateUsed(response, template_name)
