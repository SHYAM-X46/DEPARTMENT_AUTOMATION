# Generated by Django 3.2.23 on 2024-01-09 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeptautoApp', '0005_alter_students_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='date',
            field=models.CharField(default='0000-00-00', max_length=100),
        ),
        migrations.AddField(
            model_name='materials',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
