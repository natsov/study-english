# Generated by Django 5.0.6 on 2024-12-10 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_alter_lesson_content_exerciseresult_lessontheory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessontheory',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='lesson_theory/audio/'),
        ),
        migrations.AlterField(
            model_name='lessontheory',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theories', to='courses.lesson'),
        ),
        migrations.AlterField(
            model_name='lessontheory',
            name='view_type',
            field=models.CharField(choices=[('table', 'Table'), ('text', 'Text')], default='text', max_length=10),
        ),
    ]