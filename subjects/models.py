from django.db import models
from django.urls import reverse
from careers.models import Career


class Thing(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Area(Thing):
    def get_subject_count(self):
        return 'pendiente'

    def get_teacher_count(self):
        return self.teachers.all()


class Subject(Thing):
    key_code = models.CharField(max_length=11, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    semester = models.IntegerField()
    weekly_hours = models.IntegerField()
    module_number = models.IntegerField(null=True, blank=True)
    career = models.ForeignKey(Career, on_delete=models.CASCADE, null=True, blank=True)


    def get_teacher_subject(self):
        return self.teacher_subject.all()

    def get_teachers_count(self):
        return self.get_teacher_subject().count()

    def get_absolute_url(self):
        return reverse('subjects:subject-detail', kwargs={'pk': self.pk})

    def get_type(self):
        if self.career:
            return 'Modulo'
        return 'Materia'