from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Classroom


class ClassroomListView(LoginRequiredMixin, ListView):
	model = Classroom

class ClassroomCreateView(CreateView):
	model = Classroom
	fields = '__all__'
	success_url = reverse_lazy('classrooms:classroom-list')