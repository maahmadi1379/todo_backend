# Generated by Django 4.2.13 on 2024-06-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date Time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date Time')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted Date Time')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
                'db_table': 'notes',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date Time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date Time')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted Date Time')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('status', models.IntegerField(choices=[(1, 'todo'), (2, 'in_progress'), (3, 'down')])),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'tasks',
                'ordering': ['created'],
            },
        ),
    ]
