from django.urls import path, include
from rest_framework import routers 
from django.conf.urls import url
from .views import (
	book_list,
	book_create,
	book_detail,
)

urlpatterns = [
	url(r'^book_list$', book_list, name='book_list'),
	url(r'^book_create/$', book_create),
	url(r'^(?P<slug>[\w-]+)/$', book_detail, name='book_detail'),
]