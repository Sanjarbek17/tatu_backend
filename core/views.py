from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Article, SchoolYear, ProfessorProfile, StudentProfile
from .serializers import ArticleSerializer, SchoolYearSerializer
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.utils.decorators import method_decorator
from django.views import View
import json

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        if data.get('is_professor', False):
            ProfessorProfile.objects.create(user=user)
        elif data.get('is_student', False):
            StudentProfile.objects.create(user=user)

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
    def get(self, request, username):
        try:
            professor = ProfessorProfile.objects.get(user__username=username)
            articles = Article.objects.filter(professor=professor)
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)
        except ProfessorProfile.DoesNotExist:
            return Response({"error": "Professor not found"}, status=status.HTTP_404_NOT_FOUND)

class ArticleUploadView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        try:
            professor = ProfessorProfile.objects.get(user=request.user)
            data = request.data
            data['professor'] = professor.id
            serializer = ArticleSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ProfessorProfile.DoesNotExist:
            return Response({"error": "Only professors can upload articles."}, status=status.HTTP_403_FORBIDDEN)

class CustomLoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            if not request.body:
                return JsonResponse({'error': 'Empty request body'}, status=400)

            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return JsonResponse({'error': 'Username and password are required'}, status=400)

            user = authenticate(username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                user_data = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "is_professor": hasattr(user, 'professorprofile'),
                    "is_student": hasattr(user, 'studentprofile'),
                    "token": token.key
                }
                return JsonResponse(user_data, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
