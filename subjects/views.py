from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Area, Subject


class AreaListView(LoginRequiredMixin, ListView):
	model = Area

class AreaCreateView(CreateView):
	model = Area
	fields = '__all__'
	success_url = reverse_lazy('subjects:area-list')

class SubjectListView(LoginRequiredMixin, ListView):
	model = Subject

class SubjectCreateView(CreateView):
	model = Subject
	fields = '__all__'
	success_url = reverse_lazy('subjects:subject-list')

class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject
