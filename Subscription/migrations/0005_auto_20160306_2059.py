# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscription', '0004_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='type',
        ),
        migrations.AddField(
            model_name='category',
            name='type_of_competitors',
            field=models.CharField(choices=[('Beginners', 'Beginners'), ('Advanced', 'Gevorderden'), ('Kids', 'Kinderen'), ('Youth', 'Jeugd')], default='Beginners', max_length=20),
        ),
        migrations.AlterField(
            model_name='category',
            name='examination_type',
            field=models.CharField(choices=[('Form', 'Vorm'), ('Rhytm', 'Ritme'), ('Official', 'Officieel')], max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='number_of_red_ribbons',
            field=models.PositiveSmallIntegerField(choices=[(0, '0'), (1, '1'), (2, '2')]),
        ),
    ]