from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import SchoolPeriod


class SchoolPeriodListView(LoginRequiredMixin, ListView):
	model = SchoolPeriod

class SchoolPeriodCreateView(CreateView):
	model = SchoolPeriod
	fields = '__all__'
	success_url = reverse_lazy('schedules:schoolperiod-list')