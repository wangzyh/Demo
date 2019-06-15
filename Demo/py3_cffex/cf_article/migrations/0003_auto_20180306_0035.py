# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cf_article', '0002_auto_20180306_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postinfo',
            name='post_date_gmt',
            field=models.DateTimeField(),
        ),
    ]
