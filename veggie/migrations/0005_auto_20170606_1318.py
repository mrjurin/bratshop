# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0004_auto_20170606_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('status', models.BooleanField()),
                ('change_date', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veggie.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='add_date',
        ),
        migrations.AddField(
            model_name='item',
            name='change_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='change_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='oi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veggie.Item'),
        ),
        migrations.AddField(
            model_name='order',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veggie.Offer'),
        ),
    ]
