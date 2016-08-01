# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juriidilisedjuured', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='help_text_en',
            field=models.CharField(null=True, blank=True, verbose_name='help text', max_length=255),
        ),
        migrations.AddField(
            model_name='node',
            name='help_text_et',
            field=models.CharField(null=True, blank=True, verbose_name='help text', max_length=255),
        ),
        migrations.AddField(
            model_name='node',
            name='name_en',
            field=models.CharField(null=True, verbose_name='name', max_length=255),
        ),
        migrations.AddField(
            model_name='node',
            name='name_et',
            field=models.CharField(null=True, verbose_name='name', max_length=255),
        ),
    ]
