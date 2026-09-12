from django.shortcuts import render

from main.models import Education, Experience


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

def show_experience(request):
    context = {
        "name": "Rafata Zahi Cherie",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skills(request):
    context = {
        "name": "Rafata Zahi Cherie",
    }
    return render(request, "skills.html", context)

def show_contact(request):
    context = {
        "name": "Rafata Zahi Cherie",
    }
    return render(request, "contact.html", context)