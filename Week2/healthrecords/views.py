from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Patient

class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patients'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patients/patient_detail.html'
    context_object_name = 'patients'

class PatientCreateView(CreateView):
    model = Patient
    fields = ['name', 'age', 'contact', 'diagnosis', 'admission_date']
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['name', 'age', 'contact', 'diagnosis', 'admission_date']
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patients/patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')
