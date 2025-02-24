from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_query, name='weather_query'),
    path('history/', views.query_history, name='query_history'),
]