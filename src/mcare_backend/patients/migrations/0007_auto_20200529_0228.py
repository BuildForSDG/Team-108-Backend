# Generated by Django 2.2.12 on 2020-05-29 01:28

from django.conf import settings
from django.db import migrations, models
import patients.models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_messages_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(patients.models.get_custom_user), to=settings.AUTH_USER_MODEL),
        ),
    ]
