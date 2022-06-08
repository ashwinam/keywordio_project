from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import F
from django.utils import timezone   
from .models import Books
from .forms import AddForm

# Create your views here.


class IndexView(ListView):
    model = Books
    template_name = "home.html"
    context_object_name = 'books'
    paginate_by: int = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = timezone.now()
        return context

class BookDetailView(DetailView):
    model = Books
    template_name = 'book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Books.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()

        return 

class AddBookView(CreateView):
    model = Books
    form_class = AddForm
    template_name = 'add.html'
    success_url = '/books/'



class BookEditView(UpdateView):
    model = Books
    form_class = AddForm
    template_name = 'add.html'
    success_url = '/books/'