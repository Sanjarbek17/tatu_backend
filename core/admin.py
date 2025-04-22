from django.contrib import admin
from .models import (
    ProfessorProfile, StudentProfile, SchoolYear, Article, IlmiyMaqola, 
    KonferensiyaMateriali, Monografiya, OquvQollanma, OquvUslubiyQollanma, 
    AmaliyMashgulotlarMetodikQollanma, PatentIxtiro, GrantLoyiha, 
    Dissertatsiya, IlmiyTarjima, TexnikHisobot, NazariyTadqiqot, Kafedra
)

class ProfessorProfileAdmin(admin.ModelAdmin):
    list_filter = ('department',)
    search_fields = ('user__username',)

class StudentProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

class SchoolYearAdmin(admin.ModelAdmin):
    list_filter = ('start_date', 'end_date')
    search_fields = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('professor', 'school_year', 'created_at')
    search_fields = ('title',)

class IlmiyMaqolaAdmin(admin.ModelAdmin):
    list_filter = ('professor', 'kafedras', 'school_year', 'created_at')
    search_fields = ('title',)

    def get_kafedra_names(self, obj):
        return ", ".join([kafedra.name for kafedra in obj.kafedras.all()])
    get_kafedra_names.short_description = 'Kafedras'

    list_display = ('title', 'professor', 'school_year', 'get_kafedra_names')

class KonferensiyaMaterialiAdmin(admin.ModelAdmin):
    list_filter = ('is_full_text',)

class MonografiyaAdmin(admin.ModelAdmin):
    pass

class OquvQollanmaAdmin(admin.ModelAdmin):
    pass

class OquvUslubiyQollanmaAdmin(admin.ModelAdmin):
    pass

class AmaliyMashgulotlarMetodikQollanmaAdmin(admin.ModelAdmin):
    pass

class PatentIxtiroAdmin(admin.ModelAdmin):
    list_filter = ('patent_number',)

class GrantLoyihaAdmin(admin.ModelAdmin):
    list_filter = ('grant_name',)

class DissertatsiyaAdmin(admin.ModelAdmin):
    list_filter = ('degree_type',)

class IlmiyTarjimaAdmin(admin.ModelAdmin):
    list_filter = ('original_language', 'translated_language')

class TexnikHisobotAdmin(admin.ModelAdmin):
    pass

class NazariyTadqiqotAdmin(admin.ModelAdmin):
    pass

class KafedraAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(ProfessorProfile, ProfessorProfileAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(IlmiyMaqola, IlmiyMaqolaAdmin)
admin.site.register(KonferensiyaMateriali, KonferensiyaMaterialiAdmin)
admin.site.register(Monografiya, MonografiyaAdmin)
admin.site.register(OquvQollanma, OquvQollanmaAdmin)
admin.site.register(OquvUslubiyQollanma, OquvUslubiyQollanmaAdmin)
admin.site.register(AmaliyMashgulotlarMetodikQollanma, AmaliyMashgulotlarMetodikQollanmaAdmin)
admin.site.register(PatentIxtiro, PatentIxtiroAdmin)
admin.site.register(GrantLoyiha, GrantLoyihaAdmin)
admin.site.register(Dissertatsiya, DissertatsiyaAdmin)
admin.site.register(IlmiyTarjima, IlmiyTarjimaAdmin)
admin.site.register(TexnikHisobot, TexnikHisobotAdmin)
admin.site.register(NazariyTadqiqot, NazariyTadqiqotAdmin)
admin.site.register(Kafedra, KafedraAdmin)
