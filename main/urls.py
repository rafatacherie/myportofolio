from django.urls import path

from main.views import (
    show_main,
    show_education,
    show_experience,
    create_experience,
    delete_experience,
    get_experience_json,
    show_skills,
    show_contact,
    show_projects,
    create_project,
    delete_project,
    get_projects_json,
    toggle_star,
    register,
    login_user,
    logout_user,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("education/", show_education, name="show_education"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("skills/", show_skills, name="show_skills"),
    path("contact/", show_contact, name="show_contact"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]