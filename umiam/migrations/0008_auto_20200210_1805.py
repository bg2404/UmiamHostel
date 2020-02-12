# Generated by Django 3.0.3 on 2020-02-10 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('umiam', '0007_auto_20200210_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hmcmember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hmc_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
