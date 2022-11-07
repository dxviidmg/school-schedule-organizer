from django.db import models
from subjects.models import Area, Subject


class Person(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Nombre')
    last_name = models.CharField(max_length=20, verbose_name='Apellido paterno')
    second_last_name = models.CharField(max_length=20, verbose_name='Apellido materno')

    class Meta:
        abstract = True
    
    def get_full_name(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.second_last_name).strip()

    def __str__(self):
        return self.get_full_name()


class Teacher(Person):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    hours = models.IntegerField()


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)        
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #Preguntar a Pil, si año, esta bien
    year = models.IntegerField()

class ScheduleAvailability(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)    
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()
