# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-19 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poetry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='诗名')),
                ('author', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
    ]
