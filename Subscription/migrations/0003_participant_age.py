# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscription', '0002_participant_number_of_red_ribbons'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='age',
            field=models.PositiveSmallIntegerField(default=6),
        ),
    ]
