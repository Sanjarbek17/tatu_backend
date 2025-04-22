from django.contrib import admin
from .models import (
    ProfessorProfile, StudentProfile, SchoolYear, Article, IlmiyMaqola, 
    KonferensiyaMateriali, Monografiya, OquvQollanma, OquvUslubiyQollanma, 
    AmaliyMashgulotlarMetodikQollanma, PatentIxtiro, GrantLoyiha, 
    Dissertatsiya, IlmiyTarjima, TexnikHisobot, NazariyTadqiqot
)

class IlmiyMaqolaAdmin(admin.ModelAdmin):
    list_filter = ('professor', 'school_year', 'created_at')
    search_fields = ('title', 'professor__name', 'school_year__name')

admin.site.register(ProfessorProfile)
admin.site.register(StudentProfile)
admin.site.register(SchoolYear)
admin.site.register(Article)
admin.site.register(IlmiyMaqola, IlmiyMaqolaAdmin)
admin.site.register(KonferensiyaMateriali)
admin.site.register(Monografiya)
admin.site.register(OquvQollanma)
admin.site.register(OquvUslubiyQollanma)
admin.site.register(AmaliyMashgulotlarMetodikQollanma)
admin.site.register(PatentIxtiro)
admin.site.register(GrantLoyiha)
admin.site.register(Dissertatsiya)
admin.site.register(IlmiyTarjima)
admin.site.register(TexnikHisobot)
admin.site.register(NazariyTadqiqot)
