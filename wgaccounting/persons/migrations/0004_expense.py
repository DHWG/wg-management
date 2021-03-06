# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 19:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_inhabitant_system_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
