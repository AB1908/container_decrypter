# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DLC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dlc', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]