from django.urls import path
from . import views

app_name = 'http_api_app'
urlpatterns = [
    path('v1/books/all', views.http_api, name='http_api'),
	path('v1/books/<int:id>', views.http_api_by_book, name='http_api_by_book'),
	path('v1/books/<str:id>', views.http_api_by_book_error_path, name='http_api_by_book_error_path'),
]