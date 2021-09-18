from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import reverse
from django.test import TestCase
from notes.models import Item
from notes.forms import UserRegisterForm
from .factories.user import UserFactory
from .factories.item import ItemFactory

User = get_user_model()

PASSWORD = "dkfjW#498,x"


class LandingPageViewTest(TestCase):
    def setUp(self) -> None:
        self.user1 = UserFactory(password=PASSWORD)
        self.user2 = UserFactory(password=PASSWORD)
        ItemFactory(user=self.user1)
        ItemFactory(user=self.user2)

    def test_status_code(self):
        self.client.login(username=self.user1.username, password=PASSWORD)
        response = self.client.get(reverse("notes:landing-page"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        self.client.login(username=self.user1.username, password=PASSWORD)
        response = self.client.get(reverse("notes:landing-page"))
        template_name = "notes/landing.html"
        self.assertTemplateUsed(response, template_name)

    def test_get_list_of_notes_for_user(self):
        self.client.login(username=self.user1.username, password=PASSWORD)
        response = self.client.get(reverse("notes:landing-page"))
        object_list = response.context["items"]
        self.assertQuerysetEqual(object_list, self.user1.item_set.all())

    def test_anonymous_visit(self):
        response = self.client.get(reverse("notes:landing-page"))
        self.assertRedirects(response, reverse("login"))


class ItemPageViewTest(TestCase):
    def setUp(self) -> None:
        self.user1 = UserFactory(password=PASSWORD)
        self.user2 = UserFactory(password=PASSWORD)
        ItemFactory(user=self.user1)
        ItemFactory(user=self.user2)

    def test_anonymous_visit(self):
        items = Item.objects.filter(user=self.user1)
        item = items.first()
        response = self.client.get(reverse("notes:item", kwargs={"pk": item.id}))
        self.assertRedirects(response, reverse("login"))

    def test_user_visit_item(self):
        self.client.login(username=self.user2.username, password=PASSWORD)
        items = Item.objects.filter(user=self.user2)
        item = items.first()
        response = self.client.get(reverse("notes:item", kwargs={"pk": item.id}))
        response_context = response.context["item"]
        self.assertEqual(response_context, item)


class ItemCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.user1 = UserFactory(password=PASSWORD)
        self.user2 = UserFactory(password=PASSWORD)
        ItemFactory(user=self.user1)
        ItemFactory(user=self.user2)

    def test_anonymous_visit(self):
        response = self.client.get(reverse("notes:create"))
        self.assertRedirects(response, reverse("login"))

    def test_user_create_item(self):
        self.client.login(username=self.user2.username, password=PASSWORD)
        data = {
            "title": "Meeting",
            "text": "The meeting is held on Friday",
        }

        self.client.post(reverse("notes:create"), data)
        is_created = Item.objects.filter(
            user=self.user2, text=data["text"], title=data["title"]
        ).exists()
        self.assertTrue(is_created)


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
