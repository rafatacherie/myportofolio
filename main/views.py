import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from main.forms import ProjectForm, ExperienceForm
from main.models import Project, Education, Experience, Skill, Contact


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No login session / Cookie not found')
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
        "last_login": last_login,
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

    experiences_json = serializers.serialize(
        "json", experiences, use_natural_foreign_keys=True,
        fields=["title", "role", "description", "category", "thumbnail", "started_at", "ended_at"],
    )
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

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience successfully added!")
        return redirect("main:show_experience")

    context = {
        "name": "Rafata Zahi Cherie",
        "form": form,
        "is_edit": False,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not (request.user.is_superuser or request.user.groups.filter(name='Editor').exists()):
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience successfully updated!")
        return redirect("main:show_experience")

    context = {
        "name": "Rafata Zahi Cherie",
        "form": form,
        "is_edit": True,
    }
    return render(request, "experience_form.html", context)

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
    projects = Project.objects.prefetch_related("starred_by").all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Rafata Zahi Cherie",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project successfully added!")
        return redirect("main:show_projects")

    context = {
        "name": "Rafata Zahi Cherie",
        "form": form,
        "is_edit": False,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project successfully deleted!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def edit_project(request, project_id):
    if not (request.user.is_superuser or request.user.groups.filter(name='Editor').exists()):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project successfully updated!")
        return redirect("main:show_projects")

    context = {
        "name": "Rafata Zahi Cherie",
        "form": form,
        "is_edit": True,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account successfully created. Please login.")
        return redirect("main:login")

    context = {"name": "Rafata Zahi Cherie", "form": form}
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {"name": "Rafata Zahi Cherie", "form": form}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "The project was successfully added.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)