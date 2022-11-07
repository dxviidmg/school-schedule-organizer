from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Area(Thing):
#    name = models.CharField(max_length=50)
    pass


class Subject(Thing):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    semester = models.IntegerField()
    weekly_hours = models.IntegerField()
