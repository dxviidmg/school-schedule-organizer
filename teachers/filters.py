import django_filters
from django_filters import DateFilter, TimeRangeFilter, TimeFilter
from django.forms.widgets import TextInput

from .models import Teacher

class TeacherFilter(django_filters.FilterSet):
    checkin_time = TimeFilter(field_name="schedule_availability__checkin_time", label="Hora de entrada", lookup_expr='lte')
    checkout_time = TimeFilter(field_name="schedule_availability__checkout_time", label="Hora de salida", lookup_expr='gte')

    class Meta:
        model = Teacher
        fields = ['area', 'teacher_subject__subject', 'schedule_availability__monday', 'schedule_availability__tuesday', 'schedule_availability__wednesday', 'schedule_availability__thursday', 'schedule_availability__friday']