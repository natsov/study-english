# Generated by Django 5.0.6 on 2024-08-20 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='enrolled_course',
        ),
    ]
