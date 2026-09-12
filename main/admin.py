from django.contrib import admin

from .models import Education, Experience, Skill, Contact

admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Contact)