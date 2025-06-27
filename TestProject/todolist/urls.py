from django.urls import path

from todolist.views import TodoDeleteView, TodoListView, TodoUpdateView, TodoCreateView

urlpatterns = [
    path ('',TodoListView.as_view(), name = 'list'),
    path ('delete/<int:pk>/',TodoDeleteView.as_view(), name = 'delete'),
    path ('update/<int:pk>/',TodoUpdateView.as_view(), name = 'update'),
    path ('create/',TodoCreateView.as_view(), name = 'create'),
]