# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0003_auto_20171202_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='user1',
            name='picture_url',
            field=models.CharField(default=b'https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwipyey1ju3XAhUQlxQKHT5NC4YQjRwIBw&url=http%3A%2F%2Fwww.qygjxz.com%2Fheart-pic.html&psig=AOvVaw2YiYuSCife9nkUinY07s8t&ust=1512365429965376', max_length=1000),
        ),
    ]