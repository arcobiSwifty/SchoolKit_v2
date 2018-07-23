# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-22 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_nome_jsonresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='nome',
            name='tema',
            field=models.CharField(default='ros', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nome',
            name='particolarita',
            field=models.CharField(choices=[('si', 'si'), ('no', 'no')], default='no', max_length=3),
        ),
    ]