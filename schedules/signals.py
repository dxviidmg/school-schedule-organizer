from .models import Group, Class
from subjects.models import Subject

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=Group)
def post_save_group(sender, instance, created, **kwargs):
    if created:
        subjects_by_semester = Subject.objects.filter(semester=instance.semester)
        subjects = subjects_by_semester.filter(career=None)
        modules = subjects_by_semester.filter(career=instance.career)
        
        subjects = subjects | modules

        for subject in subjects:
            Class.objects.create(group=instance, subject=subject)