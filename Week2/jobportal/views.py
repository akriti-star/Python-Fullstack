from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Job

class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'

class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

class JobCreateView(CreateView):
    model = Job
    fields = ['title', 'company', 'location', 'salary', 'description']
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

class JobUpdateView(UpdateView):
    model = Job
    fields = ['title', 'company', 'location', 'salary', 'description']
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job_list')

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job_list')
