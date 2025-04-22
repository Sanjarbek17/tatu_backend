from django.contrib.auth.models import User
from django.db import models

class ProfessorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Professor: {self.user.username}"

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student: {self.user.username}"

class SchoolYear(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)
    professor = models.ForeignKey(ProfessorProfile, on_delete=models.CASCADE)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class IlmiyMaqola(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)
    professor = models.ForeignKey(ProfessorProfile, on_delete=models.CASCADE)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class KonferensiyaMateriali(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)
    is_full_text = models.BooleanField(default=False)

class Monografiya(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)

class OquvQollanma(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)

class OquvUslubiyQollanma(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)

class AmaliyMashgulotlarMetodikQollanma(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)

class PatentIxtiro(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)
    patent_number = models.CharField(max_length=100)

class GrantLoyiha(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)
    grant_name = models.CharField(max_length=255)

class Dissertatsiya(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)
    degree_type = models.CharField(max_length=50, choices=[('PhD', 'PhD'), ('DSc', 'DSc')])

class IlmiyTarjima(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)
    original_language = models.CharField(max_length=50)
    translated_language = models.CharField(max_length=50)

class TexnikHisobot(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)

class NazariyTadqiqot(models.Model):
    ilmiy_maqola = models.OneToOneField(IlmiyMaqola, on_delete=models.CASCADE)

class Kafedra(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    professors = models.ManyToManyField(ProfessorProfile, related_name='kafedras')
    ilmiy_maqolalar = models.ManyToManyField(IlmiyMaqola, related_name='kafedras')
    konferensiya_materiallari = models.ManyToManyField(KonferensiyaMateriali, related_name='kafedras')
    monografiyalar = models.ManyToManyField(Monografiya, related_name='kafedras')
    oquv_qollanmalar = models.ManyToManyField(OquvQollanma, related_name='kafedras')
    oquv_uslubiy_qollanmalar = models.ManyToManyField(OquvUslubiyQollanma, related_name='kafedras')
    amaliy_mashgulotlar_metodik_qollanmalar = models.ManyToManyField(AmaliyMashgulotlarMetodikQollanma, related_name='kafedras')
    patentlar_va_ixtirolar = models.ManyToManyField(PatentIxtiro, related_name='kafedras')
    grant_loyihalar = models.ManyToManyField(GrantLoyiha, related_name='kafedras')
    dissertatsiyalar = models.ManyToManyField(Dissertatsiya, related_name='kafedras')
    ilmiy_tarjimalar = models.ManyToManyField(IlmiyTarjima, related_name='kafedras')
    texnik_hisobotlar = models.ManyToManyField(TexnikHisobot, related_name='kafedras')
    nazariy_tadqiqotlar = models.ManyToManyField(NazariyTadqiqot, related_name='kafedras')

    def __str__(self):
        return self.name
