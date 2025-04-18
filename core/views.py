from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Article, SchoolYear, ProfessorProfile
from .serializers import ArticleSerializer, SchoolYearSerializer

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            is_professor=data.get('is_professor', False),
            is_student=data.get('is_student', False)
        )
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

class ArticleListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

class ArticleDetailView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, id):
        try:
            article = Article.objects.get(id=id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)

class SchoolYearListView(APIView):
    def get(self, request):
        school_years = SchoolYear.objects.all()
        serializer = SchoolYearSerializer(school_years, many=True)
        return Response(serializer.data)

class ProfessorArticlesView(APIView):
    def get(self, request, id):
        try:
            professor = ProfessorProfile.objects.get(id=id)
            articles = Article.objects.filter(professor=professor)
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)
        except ProfessorProfile.DoesNotExist:
            return Response({"error": "Professor not found"}, status=status.HTTP_404_NOT_FOUND)
