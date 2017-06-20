# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='media', upload_to='media/'),
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_description',
            field=models.TextField(default=''),
        ),
    ]
