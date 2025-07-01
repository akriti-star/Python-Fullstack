from django.urls import path
from .views import *

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('job/add/', JobCreateView.as_view(), name='job_add'),
    path('job/<int:pk>/edit/', JobUpdateView.as_view(), name='job_edit'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
]
