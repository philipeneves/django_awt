from django.urls import path, include
from rest_framework import routers 
from geral import views

router = routers.DefaultRouter()
router.register(r'books', views.BookView, 'geral')
router.register(r'books_users', views.BookUserView, 'geral')

urlpatterns = [        
    path('api/', include(router.urls))
]