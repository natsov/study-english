# Generated by Django 5.0.6 on 2024-11-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_testresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]