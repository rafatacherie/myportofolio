from django.test import TestCase
from django.urls import reverse


class MainTest(TestCase):

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_experience_url_is_accessible(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_content(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(
            response,
            "Product Management Class by RISTEK"
        )
        self.assertContains(
            response,
            "Dream Campus 2026"
        )
        self.assertContains(
            response,
            "Compfest 18"
        )

    def test_experience_role(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Participant")
        self.assertContains(response, "Event Staff")
        self.assertContains(response, "Direct Marketing Staff")

    def test_experience_detail(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(
            response,
            "Completed a series of studies on product and project management."
        )
        self.assertContains(
            response,
            "Experienced as an MC for seminars."
        )