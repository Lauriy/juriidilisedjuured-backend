# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('help_text', models.CharField(null=True, verbose_name='help text', max_length=255, blank=True)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='modified', auto_now=True)),
                ('parent_node', models.ForeignKey(null=True, related_name='child_nodes', to='juriidilisedjuured.Node', verbose_name='parent node', blank=True)),
            ],
        ),
    ]
