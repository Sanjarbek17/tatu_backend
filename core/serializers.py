from rest_framework import serializers
from .models import Article, SchoolYear, ProfessorProfile, StudentProfile

class ProfessorProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    class Meta:
        model = ProfessorProfile
        fields = ['id', 'username', 'email', 'bio', 'department']

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['id', 'user']

class SchoolYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolYear
        fields = ['id', 'name', 'start_date', 'end_date']
        
class ArticleSerializer(serializers.ModelSerializer):
    school_year = SchoolYearSerializer(read_only=True)
    professor = ProfessorProfileSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'file', 'created_at', 'professor', 'school_year']

class ArticleWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'file', 'created_at', 'professor', 'school_year']