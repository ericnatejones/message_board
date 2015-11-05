# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_maker', models.CharField(max_length=25)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=25)),
                ('message_maker', models.CharField(max_length=25)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ManyToManyField(to='main.Message'),
        ),
    ]
