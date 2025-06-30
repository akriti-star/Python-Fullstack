from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from librarymgmt.models import *
class BookListView(generic.ListView):
    model = Book
    template_name = 'librarymgmt/listallbooks.html'
    context_object_name = 'books'
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'librarymgmt/displaybook.html'
    context_object_name = 'book'
class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'librarymgmt/addnewbook.html'
    fields = '__all__'
    success_url = reverse_lazy('listallbooks')
class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'librarymgmt/modifybookdetails.html'
    fields = '__all__'
    success_url = reverse_lazy('listallbooks')
class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'librarymgmt/deletebook.html'
    fields = '__all__'
    success_url = reverse_lazy('listallbooks')

