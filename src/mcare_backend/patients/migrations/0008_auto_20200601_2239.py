# Generated by Django 2.2.12 on 2020-06-01 21:39

from django.conf import settings
from django.db import migrations, models
import patients.models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_auto_20200529_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='author',
            field=models.OneToOneField(blank=True, null=True, on_delete=models.SET(patients.models.get_custom_user), to=settings.AUTH_USER_MODEL),
        ),
    ]