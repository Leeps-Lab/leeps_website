# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 00:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('papers', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grant_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True, help_text='If left blank, displays as "[start date] - Present"', null=True)),
                ('description', models.TextField()),
                ('password', models.CharField(blank=True, max_length=50)),
                ('protect_papers', models.CharField(choices=[('true', 'Yes'), ('false', 'No')], max_length=10)),
                ('protect_data', models.CharField(choices=[('true', 'Yes'), ('false', 'No')], max_length=10)),
                ('protect_code', models.CharField(choices=[('true', 'Yes'), ('false', 'No')], max_length=10)),
                ('archived', models.BooleanField()),
                ('grant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Grant')),
                ('papers', models.ManyToManyField(blank=True, to='papers.Paper')),
                ('people', models.ManyToManyField(blank=True, to='people.Person')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
