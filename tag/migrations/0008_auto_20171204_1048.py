# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 05:18
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0007_auto_20171203_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='link',
            new_name='generated_tag',
        ),
        migrations.RemoveField(
            model_name='clientinfo',
            name='time',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='time',
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='client_agent',
            field=models.CharField(default=b'DZ / jaz / Zome 62.0.3202', max_length=200),
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='client_meta',
            field=jsonfield.fields.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='client_time',
            field=models.DateTimeField(default=b'2006-10-25 14:30:59', max_length=100),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_time',
            field=models.DateTimeField(default=b'2006-10-25 14:30:59', max_length=100),
        ),
    ]
