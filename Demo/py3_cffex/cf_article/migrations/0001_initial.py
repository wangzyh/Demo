# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('post_title', models.CharField(max_length=100)),
                ('post_date', models.DateTimeField()),
                ('post_date_gmt', models.TimeField()),
                ('post_author', models.CharField(max_length=20)),
                ('post_excerpt', tinymce.models.HTMLField()),
                ('post_parent', models.CharField(max_length=40)),
                ('post_status', models.BooleanField()),
                ('menu_order', models.CharField(max_length=20)),
                ('post_type', models.CharField(max_length=20)),
                ('post_mime_type', models.CharField(max_length=20)),
                ('post_modified', models.DateTimeField()),
                ('post_modified_gmt', models.TimeField()),
                ('post_content_filtered', models.BooleanField()),
                ('guid', models.CharField(max_length=128)),
                ('comment_status', models.CharField(max_length=2)),
                ('comment_count', models.IntegerField()),
                ('to_ping', models.BooleanField()),
                ('pinged', models.BooleanField()),
                ('ping_status', models.BooleanField()),
            ],
        ),
    ]
