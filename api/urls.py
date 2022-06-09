from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('apiview/', views.api_view),
    path('bookList/', views.BooksList.as_view()),
    path('bookDetail/<int:id>', views.BookDetail.as_view()),
]
