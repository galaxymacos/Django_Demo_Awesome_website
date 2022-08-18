from django.urls import path, include

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('oauth/', include("social_django.urls")),
    path('register/', views.register, name='register'),
]
