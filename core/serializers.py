from rest_framework import serializers
from .models import Article, SchoolYear

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'file', 'created_at', 'professor', 'school_year']

class SchoolYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolYear
        fields = ['id', 'name', 'start_date', 'end_date']