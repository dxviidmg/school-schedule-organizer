from django.db import models
from subjects.models import Area, Subject
from django.urls import reverse

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


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

class Hours(models.Model):
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()

    class Meta:
        abstract = True

    def clean(self):
        if self.checkin_time.minute + self.checkin_time.second + self.checkout_time.minute + self.checkout_time.second!= 0:
            raise ValidationError(_('Solo acepta minutos y segundos en 0'))            
        if self.checkout_time <= self.checkin_time:
            raise ValidationError(_('La hora de salida no puede ser menor o igual a la de entrada.'))

    def get_range(self):
        return '{}-{}'.format(self.checkin_time, self.checkout_time)

    def get_hours(self):
        return self.checkout_time.hour - self.checkin_time.hour

        
class Teacher(Person):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='teachers')
    hours = models.IntegerField()

    def get_absolute_url(self):
        return reverse('teachers:teacher-detail', kwargs={'pk': self.pk})

    def get_teacher_subject(self):
        return self.teacher_subject.all()

    def get_total_availability_hours(self):
        return self.schedule_availability.get_total()

class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_subject')        
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teacher_subject')
    #Preguntar a Pil, si año, esta bien
    year = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.teacher, self.subject)

    class Meta:
        unique_together = ['teacher', 'subject']

class ScheduleAvailability(Hours):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='schedule_availability')    
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)


    def __str__(self):
        return self.teacher.__str__()

    def get_days_availables(self):
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday]

    def count_days_availables(self):
        return sum(self.get_days_availables())
        
    def get_total(self):
        return self.get_hours() * self.count_days_availables()

    def get_days_display(self):
        l = list()
        if self.monday:
            l.append('Lunes')
        if self.tuesday:
            l.append('Martes')
        if self.wednesday:
            l.append('Miercoles')
        if self.thursday:
            l.append('Jueves')
        if self.friday:
            l.append('Viernes')

        return l