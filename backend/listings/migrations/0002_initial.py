# Generated by Django 4.2.1 on 2023-05-10 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
