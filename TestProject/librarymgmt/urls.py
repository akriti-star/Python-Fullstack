from django.urls import path

from librarymgmt import views

urlpatterns = [
    path('',views.BookListView.as_view(),name='listallbooks'),
    path('book_detail/<int:pk>',views.BookDetailView.as_view(),name='bookdetail'),
    path('add_book/',views.BookCreateView.as_view(),name='addnewbook'),
    path('modify_book/<int:pk>',views.BookUpdateView.as_view(),name='modifybook'),
    path('delete_book/<int:pk>',views.BookDeleteView.as_view(),name='deletebook'),


]