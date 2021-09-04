from django.shortcuts import reverse
from django.test import TestCase


class LandingPageViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse("landing-page"))

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_name(self):
        template_name = "notes/landing.html"
        self.assertTemplateUsed(self.response, template_name)
