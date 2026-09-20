from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm, ExperienceForm
from main.models import Project, Education, Experience, Skill, Contact


def show_main(request):
    context = {
        "name": "Rafata Zahi Cherie",
        "short_name": "Rafata",
        "npm": "2506621592",
        "bio": (
            "A student with a strong interest in digital transformation and business. "
            "Skilled in problem-solving, teamwork, and analytical thinking, with a constantly "
            "evolving knowledge of data, systems, and business processes. With a growth-oriented "
            "mindset, I am always eager to learn, take on challenges, and develop my skills."
        ),
    }
    return render(request, "index.html", context)

def show_education(request):
    context = {
        "name": "Rafata Zahi Cherie",
        "study_program": "Information System",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")


def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [exp.object for exp in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Rafata Zahi Cherie",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience successfully added!")
        return redirect("main:show_experience")

    context = {
        "name": "Rafata Zahi Cherie",
        "form": form,
    }
    return render(request, "experience_form.html", context)


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def show_skills(request):
    context = {
        "name": "Rafata Zahi Cherie",
        "hard_skills": Skill.objects.filter(skill_type='hard'),
        "soft_skills": Skill.objects.filter(skill_type='soft'),
    }
    return render(request, "skills.html", context)

def show_contact(request):
    context = {
        "name": "Rafata Zahi Cherie",
        "contact_list": Contact.objects.all(), 
    }
    return render(request, "contact.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")


def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Rafata Zahi Cherie",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)


def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project successfully added!")
        return redirect("main:show_projects")

    context = {
        "name": "Rafata Zahi Cherie",
        "form": form,
    }
    return render(request, "projects_form.html", context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project successfully deleted!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")