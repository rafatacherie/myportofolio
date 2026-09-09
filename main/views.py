from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Rafata Zahi Cherie",
        "short_name": "Rafata",
        "npm": "2506621592",
        "study_program": "Information System",
        "bio": (
            "A student with a strong interest in digital transformation and business. "
            "Skilled in problem-solving, teamwork, and analytical thinking, with a constantly "
            "evolving knowledge of data, systems, and business processes. With a growth-oriented "
            "mindset, I am always eager to learn, take on challenges, and develop my skills."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Rafata Zahi Cherie",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)