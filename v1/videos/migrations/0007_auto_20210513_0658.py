# Generated by Django 3.1.3 on 2021-05-13 06:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20210331_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('vimeo_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='PlaylistCategory',
        ),
        migrations.AlterModelOptions(
            name='playlistcategory',
            options={'ordering': ('created_date',), 'verbose_name': 'playlist_category', 'verbose_name_plural': 'playlist categories'},
        ),
        migrations.RenameField(
            model_name='video',
            old_name='duration',
            new_name='duration_seconds',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='author',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='language',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='playlist_id',
        ),
        migrations.RemoveField(
            model_name='video',
            name='author',
        ),
        migrations.RemoveField(
            model_name='video',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='video',
            name='language',
        ),
        migrations.RemoveField(
            model_name='video',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_type',
        ),
        migrations.AddField(
            model_name='video',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='playlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='videos.playlist'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.instructor'),
        ),
    ]