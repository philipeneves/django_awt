from rest_framework import routers
from geral import views as myapp_views

router = routers.DefaultRouter()
router.register(r'books', myapp_views.BookViewset)
router.register(r'books_users', myapp_views.BookUserViewset)