# Generated by Django 4.2.3 on 2024-03-17 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schletter_app', '0018_remove_about_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
    ]