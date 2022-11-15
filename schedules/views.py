from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import SchoolPeriod, Group, Class, Schedule
from .forms import ScheduleForm

class SchoolPeriodListView(LoginRequiredMixin, ListView):
	model = SchoolPeriod

class SchoolPeriodCreateView(CreateView):
	model = SchoolPeriod
	fields = '__all__'
	success_url = reverse_lazy('schedules:schoolperiod-list')

class SchoolPeriodDetailView(LoginRequiredMixin, DetailView):
	model = SchoolPeriod

class GroupDetailView(LoginRequiredMixin, DetailView):
	model = Group

class ClassUpdateView(LoginRequiredMixin, UpdateView):
	model = Class
	fields = ['teacher']

	def get_success_url(self):
		return self.get_object().group.get_absolute_url()


class ScheduleCreateView(LoginRequiredMixin, CreateView):
	model = Schedule
	form_class = ScheduleForm

	def form_valid(self, form):
		form.instance._class_id = self.kwargs['pk']
		return super().form_valid(form)

	def get_class(self):
		return Class.objects.get(pk=self.kwargs['pk'])

	def get_success_url(self):
		return self.get_class().group.get_absolute_url()