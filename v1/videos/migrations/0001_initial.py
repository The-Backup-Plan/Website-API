# Generated by Django 3.1.1 on 2021-02-10 17:22

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('playlist_id', models.CharField(editable=False, max_length=50)),
                ('items', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=11), size=None)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('published_at', models.DateTimeField()),
                ('author', models.CharField(max_length=250)),
                ('thumbnail', models.CharField(max_length=250)),
                ('language', models.CharField(max_length=250)),
                ('playlist_type', models.CharField(choices=[('youtube', 'youtube'), ('vimeo', 'vimeo')], editable=False, max_length=15)),
            ],
            options={
                'ordering': ('published_at',),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('video_id', models.CharField(editable=False, max_length=11)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('published_at', models.DateTimeField()),
                ('duration', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=250)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250, null=True), blank=True, default=list, size=500)),
                ('category', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), size=None)),
                ('thumbnail', models.CharField(max_length=250)),
                ('language', models.CharField(max_length=250)),
                ('video_type', models.CharField(choices=[('youtube', 'youtube'), ('vimeo', 'vimeo')], editable=False, max_length=15)),
            ],
            options={
                'ordering': ('published_at',),
            },
        ),
    ]