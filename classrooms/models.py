from django.db import models
from careers.models import Career


class Classroom(models.Model):
    number = models.IntegerField()
    career = models.ForeignKey(Career, on_delete=models.CASCADE, null=True, blank=True)

    def get_type(self):
        if self.career:
            return 'Laboratorio'
        return 'Salon'

    def __str__(self):
        if self.career:
            return '{} {} {}'.format(self.get_type(), self.career, self.number)
        return '{} {}'.format(self.get_type(), self.number)