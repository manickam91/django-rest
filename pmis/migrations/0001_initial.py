# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 04:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Name')),
                ('start_date', models.DateTimeField(verbose_name='Start Date')),
                ('end_date', models.DateTimeField(verbose_name='End Date')),
                ('estimated_duration', models.DurationField(verbose_name='Estimated Duration')),
            ],
            options={
                'db_table': 'project_phase',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Name')),
                ('project_code', models.CharField(max_length=32, unique=True, verbose_name='Project Code')),
                ('start_date', models.DateTimeField(verbose_name='Start Date')),
                ('end_date', models.DateTimeField(verbose_name='End Date')),
                ('estimated_duration', models.DurationField(verbose_name='Estimated Duration')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Name')),
                ('start_date', models.DateTimeField(verbose_name='Start Date')),
                ('end_date', models.DateTimeField(verbose_name='End Date')),
                ('estimated_duration', models.DurationField(verbose_name='Estimated Duration')),
                ('assignee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL)),
                ('phase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_phase', to='pmis.Phase')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_project', to='pmis.Project')),
                ('reviewer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project_task',
            },
        ),
        migrations.AddField(
            model_name='phase',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phase_project', to='pmis.Project'),
        ),
    ]
