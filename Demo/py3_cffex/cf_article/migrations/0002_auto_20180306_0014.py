# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cf_article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('post_title', models.CharField(max_length=100)),
                ('post_type', models.CharField(max_length=20)),
                ('post_mime_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='postinfo',
            name='post_mime_type',
        ),
        migrations.RemoveField(
            model_name='postinfo',
            name='post_title',
        ),
        migrations.RemoveField(
            model_name='postinfo',
            name='post_type',
        ),
    ]
