from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ArticleListView, ArticleDetailView, SchoolYearListView, ProfessorArticlesView, CustomLoginView

urlpatterns = [
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/articles/', ArticleListView.as_view(), name='article-list'),
    path('api/articles/<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('api/school-years/', SchoolYearListView.as_view(), name='school-year-list'),
    path('api/professors/<str:username>/articles/', ProfessorArticlesView.as_view(), name='professor-articles-by-username'),
    path('api/custom-login/', CustomLoginView.as_view(), name='custom-login'),
]