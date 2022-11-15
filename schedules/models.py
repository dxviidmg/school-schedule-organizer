from django.db import models
from django.urls import reverse

from careers.models import Thing, Career
from subjects.models import Subject
from teachers.models import Teacher, Hours
from classrooms.models import Classroom

# Create your models here.
class SchoolPeriod(Thing):
    pass

    def get_absolute_url(self):
        return reverse('schedules:schoolperiod-detail', kwargs={'pk': self.pk})

    def get_groups(self):
        return self.groups.all()

class Group(models.Model):
    shift_choices = ((1, 'Mañana'), (2, 'Tarde'))
    school_period = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE, related_name='groups')
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.IntegerField()
    group = models.CharField(max_length=1)
    shift = models.IntegerField(default=1, choices=shift_choices)

    def __str__(self):
        return '{} {} {} {}'.format(self.semester, self.group, self.career, self.school_period)

    def get_absolute_url(self):
        return reverse('schedules:group-detail', kwargs={'pk': self.pk})

    def get_classes(self):
        return self.classes.all()

class Class(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='classes')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.subject)

    def get_schedule_by_day(self, day):
        return self.classes.get(day=day)

    def get_schedule_monday(self):
        return self.get_schedule_by_day(1)

    def get_schedule_tuesday(self):
        return self.get_schedule_by_day(2)

    def get_schedule_wednesday(self):
        return self.get_schedule_by_day(3)

    def get_schedule_thursday(self):
        return self.get_schedule_by_day(4)

    def get_schedule_friday(self):
        return self.get_schedule_by_day(5)

class Schedule(Hours):
    day_choices = ((1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'))
    _class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='classes')
    day = models.IntegerField(choices=day_choices)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return '{} {} {}-{}'.format(self._class, self.get_day_display(), self.checkin_time, self.checkout_time)

    def hours(self):
        return '{}-{}'.format(self.checkin_time, self.checkout_time)