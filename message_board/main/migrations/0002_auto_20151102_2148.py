# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='message',
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(default=1, to='main.Message'),
            preserve_default=False,
        ),
    ]
