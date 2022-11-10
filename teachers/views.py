from .filters import TeacherFilter
from .models import Teacher, Subject, ScheduleAvailability, TeacherSubject

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from django_filters.views import FilterView
from extra_views import CreateWithInlinesView, InlineFormSetFactory


class TeacherListView(LoginRequiredMixin, ListView):
	model = Teacher

class TeacherDetailView(LoginRequiredMixin, DetailView):
	model = Teacher

class TeacherSuggestion(LoginRequiredMixin, FilterView):
	filterset_class = TeacherFilter

	def get_queryset(self):
		teachers = Teacher.objects.all()
		teacher_filter = self.filterset_class(self.request.GET, queryset=teachers)
		return teacher_filter.qs

	def get_context_data(self, **kwargs):
		context_data = super().get_context_data(**kwargs)
		context_data['teacher_filter'] = self.filterset_class(self.request.GET)

		if 'teacher_subject__subject' in self.request.GET:
			subject_id = self.request.GET['teacher_subject__subject']

		
			checkin_time = self.request.GET['checkin_time']
			checkout_time = self.request.GET['checkout_time']

			subject = Subject.objects.get(id=subject_id)
			area = subject.area
			no_experience_query = {
				'area': area, 
				'schedule_availability__checkin_time__lte': checkin_time, 
				'schedule_availability__checkout_time__gte': checkout_time
			}

			no_time_query = {
				'area': area, 
				'teacher_subject__subject': subject, 
				'schedule_availability__checkout_time__gte': checkout_time
			}
			teachers_no_experience = Teacher.objects.filter(**no_experience_query).exclude(id__in=self.get_queryset())
			teachers_no_time = Teacher.objects.filter(**no_time_query).exclude(id__in=self.get_queryset())

			context_data['teachers_no_experience'] = teachers_no_experience
			context_data['teachers_no_time'] = teachers_no_time

		if self.request.GET == {}:
			context_data['all'] = True
#			self.get_queryset = []

		return context_data


class IdentificationInline(InlineFormSetFactory):
	model = ScheduleAvailability
	fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'checkin_time', 'checkout_time']


class TeacherCreationView(CreateWithInlinesView):
	model = Teacher
	fields = ['area', 'first_name', 'last_name', 'hours']
	inlines = [IdentificationInline]

class TeacherSubjectCreateView(LoginRequiredMixin, CreateView):
	model = TeacherSubject
	fields = ['subject', 'year']

	def get_object(self):
		return Teacher.objects.get(id=self.kwargs.get('pk'))

	def form_valid(self, form):
		teacher = self.get_object()

		form.instance.teacher = teacher
		return super(TeacherSubjectCreateView, self).form_valid(form)

	def get_success_url(self):        
		return self.get_object().get_absolute_url()

	def get_context_data(self, **kwargs):
		kwargs['teacher'] = self.get_object()
		return super().get_context_data(**kwargs)