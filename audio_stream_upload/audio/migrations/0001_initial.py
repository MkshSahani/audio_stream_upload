# Generated by Django 3.1.5 on 2021-02-18 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioDataUser',
            fields=[
                ('audio_file_id', models.AutoField(primary_key=True, serialize=False)),
                ('time_of_upload', models.DateTimeField(auto_now_add=True)),
                ('audio_title', models.CharField(max_length=120)),
                ('audio_file', models.URLField()),
                ('upload_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_audio', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
