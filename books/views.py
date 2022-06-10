from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Books
from .forms import AddForm

# Create your views here.


class IndexView(ListView):
    model = Books
    template_name = "home.html"
    context_object_name = 'books'
    paginate_by: int = 3

# class BookDetailView(DetailView):
#     model = Books
#     template_name = 'book-detail.html'
#     context_object_name = 'book'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         post = Books.objects.filter(slug=self.kwargs.get('slug'))
#         post.update(count=F('count') + 1)

#         context['time'] = timezone.now()

#         return 

class AddBookView(PermissionRequiredMixin, CreateView):

    raise_exception: bool = False
    login_url: str = 'http://127.0.0.1:8000/accounts/login'
    permission_required = 'books.add_books'

    model = Books
    form_class = AddForm
    template_name = 'addbooks.html'
    success_url = '/'



class BookEditView(PermissionRequiredMixin, UpdateView):
    raise_exception: bool = False
    login_url: str = 'http://127.0.0.1:8000/accounts/login'
    permission_required = 'books.change_books'

    model = Books
    form_class = AddForm
    template_name = 'editbooks.html'
    success_url = '/'

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    raise_exception: bool = False
    login_url: str = 'http://127.0.0.1:8000/accounts/login'
    permission_required = 'books.delete_books'

    model = Books
    success_url = '/'
