from django.urls import path
from . import views
urlpatterns = [
    path('TestAuth/', views.TestAuth, name='TesteAuth'),
]