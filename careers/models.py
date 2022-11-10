from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Career(Thing):
    pass