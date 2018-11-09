# Generated by Django 2.1.2 on 2018-11-09 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StravaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('access_token', fernet_fields.fields.EncryptedTextField()),
                ('expires_at', models.IntegerField(null=True)),
                ('refresh_token', fernet_fields.fields.EncryptedTextField()),
                ('athlete_id', models.IntegerField(null=True)),
                ('fetched', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'scraper_strava_token',
            },
        ),
    ]