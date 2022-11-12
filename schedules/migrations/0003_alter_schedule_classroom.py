# Generated by Django 3.2.16 on 2022-11-11 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0002_alter_classroom_unique_together'),
        ('schedules', '0002_alter_class_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classrooms.classroom'),
        ),
    ]
