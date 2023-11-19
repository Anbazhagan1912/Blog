from django.urls import path, include
from .views import BlogApi

urlpatterns = [
    path('home/', BlogApi.as_view()),
]
