# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0016_order_confirm_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='add_date',
            field=models.DateTimeField(),
        ),
    ]
