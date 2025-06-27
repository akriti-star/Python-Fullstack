from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from todolist.models import Todo
class TodoListView(generic.ListView):
    model = Todo
    template_name = 'list.html'
    context_object_name = 'todos'

class TodoCreateView(generic.CreateView):
    model = Todo
    template_name = 'create.html'
    fields = '__all__'
    success_url =  reverse_lazy('list')
class TodoUpdateView(generic.UpdateView):
    model = Todo
    template_name = 'update.html'
    fields = '__all__'
    context_object_name = 'task'
    success_url = reverse_lazy('list')
class TodoDeleteView(generic.DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
    context_object_name = 'task'
