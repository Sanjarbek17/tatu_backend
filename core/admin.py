from django.contrib import admin
from .models import ProfessorProfile, StudentProfile, SchoolYear, Article


admin.site.register(ProfessorProfile)
admin.site.register(StudentProfile)
admin.site.register(SchoolYear)
admin.site.register(Article)
