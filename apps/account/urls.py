from django.conf.urls import url, include

from apps.account import views

urlpatterns = [
    url(r'login/', views.movie_login, name='login'),
    url(r'register/', views.movie_register, name='register'),
    url(r'logout/', views.movie_logout, name='logout'),
]
