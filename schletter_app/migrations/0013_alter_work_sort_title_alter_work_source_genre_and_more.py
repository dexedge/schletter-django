# Generated by Django 4.2.3 on 2024-03-10 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schletter_app', '0012_alter_event_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='sort_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='source_genre',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='source_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
