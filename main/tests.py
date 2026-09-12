from django.test import TestCase
from django.urls import reverse

from main.models import Education, Experience, Skill


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

    def test_experience_empty_state(self):
        Experience.objects.all().delete()
        self.assertEqual(Education.objects.count(), 0)
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")


class EducationTest(TestCase):
    """Test untuk halaman Education"""

    def setUp(self):
        Education.objects.create(
            institution="Universitas Indonesia",
            program="Information System, Faculty of Computer Science",
            start_year=2025,
        )
        Education.objects.create(
            institution="MAN 2 Kota Bogor",
            program="Science",
            start_year=2022,
            end_year=2025,
        )

    def test_education_url_is_accessible(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

    def test_education_content(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "Universitas Indonesia")
        self.assertContains(response, "MAN 2 Kota Bogor")
        self.assertContains(response, "2025 - Present")
        self.assertContains(response, "2022 - 2025")

    def test_education_empty_state(self):
            Education.objects.all().delete()
            self.assertEqual(Education.objects.count(), 0)
            response = self.client.get(reverse("main:show_education"))
    
            self.assertContains(response, "Belum ada riwayat pendidikan yang ditambahkan.")

class SkillsTest(TestCase):
    """Test untuk halaman Skills"""

    def setUp(self):
        Skill.objects.create(
            name="Python",
            percentage=70,
            icon_class="bxl-python",
            skill_type="technical"
        )
        Skill.objects.create(
            name="Public Speaking",
            percentage=80,
            icon_class="bx-group",
            skill_type="soft"
        )

    def test_skills_url_is_accessible(self):
        response = self.client.get(reverse("main:show_skills"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills.html")

    def test_skills_content(self):
        response = self.client.get(reverse("main:show_skills"))
        
        self.assertContains(response, "Python")
        self.assertContains(response, "70%")
        self.assertContains(response, "Public Speaking")
        self.assertContains(response, "80%")

    def test_skills_empty_state(self):
        Skill.objects.all().delete()
        self.assertEqual(Skill.objects.count(), 0)
        response = self.client.get(reverse("main:show_skills"))

        self.assertContains(response, "Belum ada technical skills yang ditambahkan.")
        self.assertContains(response, "Belum ada soft skills yang ditambahkan.")
