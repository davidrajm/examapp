# Generated by Django 3.0.6 on 2020-05-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20200508_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='mark',
            field=models.PositiveIntegerField(default=0, verbose_name='Marks'),
        ),
    ]
