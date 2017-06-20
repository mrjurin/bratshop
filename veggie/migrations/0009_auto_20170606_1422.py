# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0008_auto_20170606_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_email',
            field=models.EmailField(default='peter.gastinger@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_name',
            field=models.CharField(default='Peter', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_phone',
            field=models.CharField(default='Gastinger', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_surname',
            field=models.CharField(default='Test', max_length=20),
            preserve_default=False,
        ),
    ]
