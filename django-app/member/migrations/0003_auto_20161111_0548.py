# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 05:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20161111_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='following',
            name='followee',
        ),
        migrations.RemoveField(
            model_name='following',
            name='follower',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='following_users',
            field=models.ManyToManyField(related_name='follower_users', through='member.Relationship', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Following',
        ),
        migrations.AddField(
            model_name='relationship',
            name='followee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationship_set_following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='relationship',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationship_set_follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
