# Generated by Django 3.2.23 on 2024-02-10 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeptautoApp', '0010_rename_marks_marks_sem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='SUBJECT_ASSIGNED_TEACHERS',
        ),
    ]
