# Generated by Django 3.1.7 on 2021-04-12 20:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('schletter_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]