from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Career


class CareerListView(LoginRequiredMixin, ListView):
	model = Career

class CareerCreateView(CreateView):
	model = Career
	fields = '__all__'
	success_url = reverse_lazy('careers:career-list')