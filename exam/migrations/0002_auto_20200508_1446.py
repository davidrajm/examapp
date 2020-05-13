# Generated by Django 3.0.6 on 2020-05-08 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='date_open',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Opening Date and Time'),
        ),
        migrations.AddField(
            model_name='exam',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
