from rest_framework import serializers
from .models import Article, SchoolYear

class SchoolYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolYear
        fields = ['id', 'name', 'start_date', 'end_date']
        
class ArticleSerializer(serializers.ModelSerializer):
    school_year = SchoolYearSerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'file', 'created_at', 'professor', 'school_year']
