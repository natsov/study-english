# Generated by Django 5.0.6 on 2024-09-30 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishLevelInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
