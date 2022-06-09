from django.urls import path
from .views import BookDeleteView, IndexView, AddBookView, BookEditView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('add/', AddBookView.as_view(), name='add-book'),
    # path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    path('<slug:slug>/edit', BookEditView.as_view(), name='edit-book'),
    path('<slug:slug>/edit/delete', BookDeleteView.as_view(), name='delete-book'),
]