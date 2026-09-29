from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select, TextInput, Textarea, URLInput, DateInput
from django.utils.html import strip_tags

from main.models import Experience, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Project Name",
            "description": "Project Description",
            "tech_stack": "Technology Used",
            "project_url": "Project URL",
            "project_image_url": "Project Image URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your project",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("The project name cannot consist solely of HTML tags.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class ExperienceForm(ModelForm):
    started_at = forms.DateField(
        label="Start Date",
        input_formats=["%Y-%m"],
        widget=forms.DateInput(attrs={"type": "month"}, format="%Y-%m"),
    )
    ended_at = forms.DateField(
        label="End Date",
        required=False,
        input_formats=["%Y-%m"],
        widget=forms.DateInput(
            attrs={"type": "month", "placeholder": "Leave empty if ongoing"},
            format="%Y-%m",
        ),
        help_text="Leave this empty if the experience is still ongoing.",
    )

    class Meta:
        model = Experience
        fields = [
            "title",
            "role",
            "description",
            "category",
            "started_at",
            "ended_at",
            "thumbnail",
        ]
 
        labels = {
            "title": "Name of Experience",
            "role": "Position/Role",
            "description": "Experience Description",
            "category": "Experience Category",
            "thumbnail": "Image URL",
        }
 
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Seminar",
                    "maxlength": 255,
                }
            ),
            "role": TextInput(
                attrs={
                    "placeholder": "Participant",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your experience",
                    "rows": 3,
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }