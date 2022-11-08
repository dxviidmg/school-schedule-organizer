from django.db import models
from django.urls import reverse


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
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    semester = models.IntegerField()
    weekly_hours = models.IntegerField()


    def get_teacher_subject(self):
        return self.teacher_subject.all()

    def get_teachers_count(self):
        return self.get_teacher_subject().count()

    def get_absolute_url(self):
        return reverse('subjects:subject-detail', kwargs={'pk': self.pk})