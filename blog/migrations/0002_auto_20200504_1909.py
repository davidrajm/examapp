# Generated by Django 3.0.6 on 2020-05-04 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data_modified',
            new_name='date_modified',
        ),
    ]