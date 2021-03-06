# Generated by Django 3.1.7 on 2021-04-17 15:30

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_names', models.CharField(max_length=200)),
                ('birth', models.IntegerField()),
                ('death', models.IntegerField()),
                ('notes', models.TextField()),
            ],
            options={
                'ordering': ['last_name', 'first_names'],
            },
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_names', models.CharField(max_length=200)),
                ('birth', models.IntegerField()),
                ('death', models.IntegerField()),
                ('notes', models.TextField()),
            ],
            options={
                'ordering': ['last_name', 'first_names'],
            },
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('theater', models.CharField(max_length=3)),
                ('company', models.CharField(max_length=10)),
                ('event_type', models.CharField(max_length=50)),
                ('hadamowsky', models.CharField(max_length=5)),
                ('morrow', models.CharField(max_length=5)),
                ('notes', tinymce.models.HTMLField(blank=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schletter_app.date')),
            ],
            options={
                'ordering': ['date', 'theater'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sort_title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('notes', tinymce.models.HTMLField()),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['sort_title'],
            },
        ),
        migrations.CreateModel(
            name='WorkEvent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schletter_app.event')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schletter_app.work')),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='events',
            field=models.ManyToManyField(through='schletter_app.WorkEvent', to='schletter_app.Event'),
        ),
        migrations.CreateModel(
            name='ComposerWork',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=100)),
                ('composer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schletter_app.composer')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schletter_app.work')),
            ],
        ),
        migrations.AddField(
            model_name='composer',
            name='works',
            field=models.ManyToManyField(related_name='composerworks', through='schletter_app.ComposerWork', to='schletter_app.Work'),
        ),
        migrations.CreateModel(
            name='AuthorWork',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schletter_app.author')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schletter_app.work')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='works',
            field=models.ManyToManyField(related_name='authorworks', through='schletter_app.AuthorWork', to='schletter_app.Work'),
        ),
    ]
