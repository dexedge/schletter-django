# Generated by Django 4.2.3 on 2024-03-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schletter_app', '0016_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='slug',
            field=models.SlugField(default='about'),
        ),
    ]