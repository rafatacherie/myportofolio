from django.test import TestCase
from django.urls import reverse

from main.models import Experience


class MainTest(TestCase):
    """Test untuk halaman profil (index.html)"""

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)


class ExperienceTest(TestCase):
    """Test untuk halaman Experience"""

    def setUp(self):
        Experience.objects.create(
            title="Product Management Class by RISTEK",
            role="Participant",
            category="volunteer",
            description="Completed a series of studies on product and project management.",
        )
        Experience.objects.create(
            title="Dream Campus 2026",
            role="Event Staff",
            category="volunteer",
            description="Responsible for planning, coordinating, and executing a series of events.",
        )
        Experience.objects.create(
            title="Compfest 18",
            role="Direct Marketing Staff",
            category="volunteer",
            description="Experienced as an MC for seminars.",
        )

    def test_experience_url_is_accessible(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")

    def test_experience_content(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Product Management Class by RISTEK")
        self.assertContains(response, "Dream Campus 2026")
        self.assertContains(response, "Compfest 18")

    def test_experience_role(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Participant")
        self.assertContains(response, "Event Staff")
        self.assertContains(response, "Direct Marketing Staff")

    def test_experience_detail(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(
            response,
            "Completed a series of studies on product and project management.",
        )
        self.assertContains(response, "Experienced as an MC for seminars.")