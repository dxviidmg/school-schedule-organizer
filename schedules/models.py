from django.db import models
from careers.models import Thing, Career
from subjects.models import Subject
from teachers.models import Teacher
from classrooms.models import Classroom

# Create your models here.
class SchoolPeriod(Thing):
    pass

class Group(models.Model):
    shift_choices = ((1, 'Mañana'), (2, 'Tarde'))
    school_period = models.ForeignKey(SchoolPeriod, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.IntegerField()
    group = models.CharField(max_length=1)
    shift = models.IntegerField(default=1, choices=shift_choices)

    def __str__(self):
        return '{} {} {} {}'.format(self.semester, self.group, self.career, self.school_period)

class Class(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.group, self.subject)


class Schedule(models.Model):
    day_choices = ((1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'))
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    day = models.IntegerField(choices=day_choices)
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True)
